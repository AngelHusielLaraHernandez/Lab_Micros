from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import cv2


BASE_DIR = Path(__file__).resolve().parent
VIDEO_DIR = BASE_DIR / "video"
OUTPUT_DIR = BASE_DIR / "image_video"
SUPPORTED_VIDEO_EXTENSIONS = (".mp4", ".avi", ".mov", ".mkv", ".m4v", ".wmv", ".webm")


def parse_time_value(raw_value: str) -> float:
    value = raw_value.strip()
    if not value:
        raise ValueError("El tiempo no puede estar vacío.")

    if re.fullmatch(r"\d+(?:\.\d+)?", value):
        return float(value)

    parts = value.split(":")
    if len(parts) not in (2, 3):
        raise ValueError(
            "Usa segundos como número o formato HH:MM:SS / MM:SS."
        )

    try:
        numbers = [float(part) for part in parts]
    except ValueError as exc:
        raise ValueError(
            "El tiempo debe contener solo números separados por dos puntos."
        ) from exc

    if len(numbers) == 2:
        minutes, seconds = numbers
        return minutes * 60 + seconds

    hours, minutes, seconds = numbers
    return hours * 3600 + minutes * 60 + seconds


def prompt_for_value(message: str, parser) -> float:
    while True:
        raw_value = input(message).strip()
        try:
            return parser(raw_value)
        except ValueError as exc:
            print(f"Entrada inválida: {exc}")


def resolve_video_path(video_argument: str) -> Path:
    candidate = Path(video_argument.strip().strip('"').strip("'"))
    if candidate.is_file():
        return candidate

    if candidate.suffix:
        direct_match = VIDEO_DIR / candidate.name
        if direct_match.is_file():
            return direct_match

    if not candidate.suffix:
        for extension in SUPPORTED_VIDEO_EXTENSIONS:
            match = VIDEO_DIR / f"{candidate.name}{extension}"
            if match.is_file():
                return match

    if candidate.parent == Path(".") or not candidate.is_absolute():
        search_name = candidate.name
        for file_path in sorted(VIDEO_DIR.glob("*")):
            if file_path.is_file() and file_path.name == search_name:
                return file_path
            if file_path.is_file() and file_path.stem == search_name:
                return file_path

    raise FileNotFoundError(
        f"No se encontró el video '{video_argument}'. Colócalo en la carpeta 'video' o usa una ruta válida."
    )


def prepare_output_directory() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for existing_file in OUTPUT_DIR.glob("image*.png"):
        if existing_file.is_file():
            existing_file.unlink()


def extract_frames(video_path: Path, start_time: float, end_time: float) -> int:
    capture = cv2.VideoCapture(str(video_path))
    if not capture.isOpened():
        raise RuntimeError(f"No se pudo abrir el video: {video_path}")

    fps = capture.get(cv2.CAP_PROP_FPS)
    if not fps or fps <= 0:
        capture.release()
        raise RuntimeError("No se pudo detectar la tasa de fotogramas del video.")

    total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    start_frame = max(0, int(round(start_time * fps)))
    end_frame = max(start_frame, int(round(end_time * fps)))

    if total_frames > 0:
        last_valid_frame = max(0, total_frames - 1)
        if start_frame > last_valid_frame:
            capture.release()
            raise ValueError(
                "El tiempo de inicio queda fuera de la duración del video."
            )
        end_frame = min(end_frame, last_valid_frame)

    capture.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    saved_count = 0
    current_frame = start_frame

    while current_frame <= end_frame:
        success, frame = capture.read()
        if not success:
            break

        output_path = OUTPUT_DIR / f"image{saved_count + 1}.png"
        if not cv2.imwrite(str(output_path), frame):
            capture.release()
            raise RuntimeError(f"No se pudo guardar la imagen: {output_path}")

        saved_count += 1
        current_frame += 1

    capture.release()

    if saved_count == 0:
        raise RuntimeError("No se extrajo ningún fotograma en el intervalo indicado.")

    return saved_count


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Extrae fotogramas de un video dentro de la carpeta video y los guarda "
            "como image1.png, image2.png, etc."
        )
    )
    parser.add_argument(
        "video",
        nargs="?",
        help="Nombre o ruta del video. Si se omite, se preguntará por terminal.",
    )
    parser.add_argument(
        "--inicio",
        help="Tiempo inicial en segundos o formato HH:MM:SS / MM:SS.",
    )
    parser.add_argument(
        "--fin",
        help="Tiempo final en segundos o formato HH:MM:SS / MM:SS.",
    )
    return parser


def main() -> int:
    parser = build_argument_parser()
    args = parser.parse_args()

    if args.video:
        video_argument = args.video
    else:
        video_argument = input("Nombre del video dentro de la carpeta 'video': ").strip()

    try:
        video_path = resolve_video_path(video_argument)
    except (FileNotFoundError, ValueError) as exc:
        print(exc)
        return 1

    if args.inicio is not None:
        try:
            start_time = parse_time_value(args.inicio)
        except ValueError as exc:
            print(f"Tiempo inicial inválido: {exc}")
            return 1
    else:
        start_time = prompt_for_value(
            "Tiempo inicial (segundos o HH:MM:SS): ", parse_time_value
        )

    if args.fin is not None:
        try:
            end_time = parse_time_value(args.fin)
        except ValueError as exc:
            print(f"Tiempo final inválido: {exc}")
            return 1
    else:
        end_time = prompt_for_value(
            "Tiempo final (segundos o HH:MM:SS): ", parse_time_value
        )

    if start_time < 0 or end_time < 0:
        print("Los tiempos no pueden ser negativos.")
        return 1

    if end_time <= start_time:
        print("El tiempo final debe ser mayor que el tiempo inicial.")
        return 1

    prepare_output_directory()

    try:
        saved_count = extract_frames(video_path, start_time, end_time)
    except (RuntimeError, ValueError) as exc:
        print(exc)
        return 1

    print(f"Video procesado: {video_path}")
    print(f"Fotogramas guardados en: {OUTPUT_DIR}")
    print(f"Total de imágenes creadas: {saved_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
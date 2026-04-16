#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import requests
import time


def main():

    parser = argparse.ArgumentParser(description='ESA1 Audiorekorder')
    parser.add_argument('url', help='URL des Streams')
    parser.add_argument('--filename', default='myRadio.mp3', help='Dateiname')
    parser.add_argument('--duration', type=int, default=30, help='Dauer in Sekunden')
    parser.add_argument('--blocksize', type=int, default=64, help='Blockgröße in Bytes')
    parser.add_argument('--list', action='store_true', help='Zeige alle gespeicherten MP3-Dateien an')

    args = parser.parse_args()
    if args.list:
        import os
        files = [f for f in os.listdir('.') if f.endswith('.mp3')]
        print("Gespeicherte Streams:", files)
        return

    try:
        response = requests.get(args.url, stream=True, timeout=10)
        response.raise_for_status()

        with open(args.filename, 'wb') as f:
            start_time = time.time()
            print(f"Aufnahme läuft für {args.duration}s...")

            for block in response.iter_content(chunk_size=args.blocksize):
                if time.time() - start_time > args.duration:
                    break
                if block:
                    f.write(block)

        print(f"Fertig! Datei gespeichert als: {args.filename}")

    except Exception as e:
        print(f"Fehler bei der Aufnahme: {e}")


if __name__ == "__main__":
    main()
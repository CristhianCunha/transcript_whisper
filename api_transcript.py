import tempfile
import os
import logging
import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import base64
import io
import uvicorn
import whisper
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
model = whisper.load_model("medium")

APIKEY = os.getenv("APIKEY")


class AudioBase64(BaseModel):
    audio_base64: str
    apiKey: str


@app.post("/transcribe/")
async def transcribe_audio(audio: AudioBase64):
    if audio.apiKey != APIKEY:
        logger.warning("Unauthorized access attempt with invalid API key.")
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API key.")

    try:
        audio_data = base64.b64decode(audio.audio_base64)
    except Exception as e:
        logger.error(f"Erro ao decodificar base64: {e}")
        raise HTTPException(
            status_code=400, detail="Erro ao decodificar base64 do áudio."
        )

    try:
        temp_dir = tempfile.gettempdir()
        temp_file_path = os.path.join(temp_dir, "temp_audio.ogg")

        with open(temp_file_path, "wb") as tmp_file:
            tmp_file.write(audio_data)
        logger.info(f"Arquivo temporário salvo em: {temp_file_path}")

        await asyncio.sleep(1)  # Manter a pausa por precaução
        logger.info(f"Tentando transcrever o arquivo: {temp_file_path}")
        transcript = model.transcribe(temp_file_path)
        os.remove(temp_file_path)
        logger.info(f"Transcrição concluída.")
        return JSONResponse({"transcription": transcript["text"]})

    except Exception as e:
        logger.error(f"Erro ao processar o áudio: {e}")
        raise HTTPException(status_code=500, detail=f"Erro ao processar o áudio: {e}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8085)

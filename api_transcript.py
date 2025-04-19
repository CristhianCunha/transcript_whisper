import tempfile
import os
import logging
import asyncio
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
import whisper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
model = whisper.load_model("medium")

@app.post("/transcribe/")
async def transcribe_audio(audio_file: UploadFile = File(...)):
    if not audio_file.filename.endswith(('.mp3', '.wav', '.ogg', '.flac', '.m4a')):
        raise HTTPException(status_code=400, detail="Formato de arquivo de áudio não suportado. Use MP3, WAV, OGG, FLAC ou M4A.")

    try:
        temp_dir = tempfile.gettempdir()
        base, ext = os.path.splitext(audio_file.filename)
        temp_file_path = os.path.join(temp_dir, f"temp_{base}{ext}")

        with open(temp_file_path, "wb") as tmp_file:
            while contents := await audio_file.read(1024):
                tmp_file.write(contents)
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
    uvicorn.run(app, host="0.0.0.0", port=8000)
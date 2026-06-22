import cloudinary.uploader

from sqlalchemy.orm import Session

from app.repositories.media_repository import (
    MediaRepository
)


class MediaService:

    @staticmethod
    async def upload_file(
        db: Session,
        file,
        uploaded_by: str | None = None,
        folder: str | None = None
    ):

        result = cloudinary.uploader.upload(
            file.file,
            folder=f"rubel-mart/{folder}"
        )

        media = MediaRepository.create(
            db,
            {
                "public_id": result["public_id"],
                "url": result["secure_url"],
                "original_name": file.filename,
                "mime_type": file.content_type,
                "size": result.get(
                    "bytes",
                    0
                ),
                "provider": "cloudinary",
                "uploaded_by": uploaded_by
            }
        )

        return media
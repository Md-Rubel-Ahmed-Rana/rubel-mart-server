from sqlalchemy.orm import Session

from app.models.media import Media


class MediaRepository:

    @staticmethod
    def create(
        db: Session,
        payload: dict
    ):

        media = Media(**payload)

        db.add(media)

        db.commit()

        db.refresh(media)

        return media
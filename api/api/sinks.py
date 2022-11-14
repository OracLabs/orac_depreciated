import fastapi

from api import db
import sqlmodel as sqlm

router = fastapi.APIRouter()


class Sink(sqlm.SQLModel, table=True):
    id: int | None = sqlm.Field(default=None, primary_key=True)
    name: str
    protocol: str
    url: str


@router.post("/")
def create_sink(sink: Sink):
    with db.session() as session:
        session.add(sink)
        session.commit()
        session.refresh(sink)
        return sink


@router.get("/", response_model=list[Sink])
def read_sinks(offset: int = 0, limit: int = fastapi.Query(default=100, lte=100)):
    with db.session() as session:
        sinks = session.exec(sqlm.select(Sink).offset(offset).limit(limit)).all()
        return sinks


@router.get("/{sink_id}")
def read_sink(sink_id: int):
    with db.session() as session:
        sink = session.get(Sink, sink_id)
        if not sink:
            raise fastapi.HTTPException(status_code=404, detail="Sink not found")
        return sink

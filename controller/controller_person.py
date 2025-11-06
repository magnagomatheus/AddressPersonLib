from fastapi import HTTPException
from sqlmodel import Session, select
from controller.controller_generic import create_crud_router, Hooks
from Lib.model.models import Person, Address
from Lib.model.dto import PersonCreate, PersonUpdate, PersonRead


class PersonHooks(Hooks[Person, PersonCreate, PersonUpdate]):
    def pre_create(self, payload: PersonCreate, session: Session) -> None:
        if payload.address_id is not None and payload.address_id != 0:
            if not session.get(Address, payload.address_id):
                raise HTTPException(400, "Address do not exists")
    
    def pre_update(self, payload: PersonUpdate, session: Session, obj: Person) -> None:
        # se vai alterar team_id, valida
        if payload.address_id is not None:
            if payload.address_id != 0 and not session.get(Address, payload.address_id):
                raise HTTPException(400, "Address do not exists")

router = create_crud_router(
    model=Person,
    create_schema=PersonCreate,
    update_schema=PersonUpdate,
    read_schema=PersonRead,
    prefix="/persons",
    tags=["persons"],
    hooks=PersonHooks(),
)

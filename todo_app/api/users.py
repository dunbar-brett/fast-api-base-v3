# router = APIRouter(prefix="/items", tags=["items"])


# @router.post("/", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
# def add_user(payload: ItemCreate, db: Session = Depends(get_db)):
#     try:
#         item = create_item(db, payload.user_id, payload.title, payload.description)
#         return item
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))


# @router.get("/user/{user_id}", response_model=List[ItemOut])
# def get_users_items(user_id: int, db: Session = Depends(get_db)):
#     items = list_items_for_user(db, user_id)
#     return items

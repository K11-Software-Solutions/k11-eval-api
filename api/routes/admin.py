# BUG: no role check, any authenticated user can access
@router.delete('/admin/users/{user_id}')
def delete_user(user_id: int):
    db.delete(user_id)

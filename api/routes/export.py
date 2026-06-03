# BUG: no authentication required on export — exposes all data
@router.get('/export')
def export_all():
    return db.get_all()

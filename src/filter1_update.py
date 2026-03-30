from sqlalchemy import update
from src.db_manager.database import engine, init_db

def mark_filtered_as_selected(title_list, table_name="EMNLP_2025"):
    if not title_list:
        return
    
    table = init_db(table_name)

    unique_titles = list(set(title_list))

    stmt = (
        update(table)
        .where(table.c.title.in_(unique_titles))
        .values(selected=1)
    )

    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()
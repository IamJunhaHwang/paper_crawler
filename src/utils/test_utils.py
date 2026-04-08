from db_manager.database import Engine, text

def for_test(table_name: str, engine: Engine):
    with engine.begin() as conn:
    # 서브쿼리(Subquery)를 사용하여 첫 10개의 ID를 찾고, 그 줄만 업데이트합니다.
        query = text(f"""
            UPDATE {table_name}
            SET selected = 1
            WHERE id IN (
                SELECT id FROM {table_name}
                ORDER BY id
                LIMIT 10
            )
        """)
        conn.execute(query)
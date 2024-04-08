from sqlalchemy import Table, Column, Integer, String, Date

from database import metadata


operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantity", String, ),
    Column("figi", String, ),
    Column("instrument_type", String, nullable=False),
    Column("date", Date),
    Column("type", String),
)
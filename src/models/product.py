class Product(Base):
    __tablename__ = 'products'
    id = column(Integer, primary_key=True)
    
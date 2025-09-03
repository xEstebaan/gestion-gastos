from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    fecha_compra = db.Column(db.Date, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categoria.id"), nullable=False)


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(120), nullable=False)

    productos = db.relationship("Producto", backref="categoria", lazy=True)

    def __repr__(self):
        return f"<Categoria {self.nombre}>"

# -*- coding: utf-8 -*-
db.define_table('Colores',
                Field('color','string'),
                format='%(color)s',
                )
db.define_table('Transmisiones',
                Field('codigo','string'),
                Field('descripcion','string'),
                format='%(codigo)s',
                singular='Trasmisión',plural='Trasmisiones',
                redefine=True,
               )
db.define_table('Automoviles',
                Field('codigo','string'),
                Field('placas', 'string'),
                Field('transmision', 'reference Transmisiones'),
                Field('color','reference Colores'),
                format='%(codigo)s',
                singular='Automóvil',plural='Automóviles',
                redefine=True,
               )
db.define_table('Rentas',
                Field('inicio', 'datetime'),
                Field('fin','datetime'),
                Field('automovil','reference Automoviles'),
                Field('cliente', 'reference Contactos'),
                Field('vendedor','reference Contactos'),
                Field('operador','reference Contactos'),
                Field('tarifa','double'),
                format='%(automovil)s',
               )
db.define_table('Transacciones_tipo',
                Field('tipo','string'),
                Field('codigo','string'),
                singular='Tipo de Transacción',plural='Tipos de Transacciones',
                format='%(codigo)s',
                )
db.define_table('Transacciones',
                Field('tipo','reference Transacciones_tipo'),
                Field('renta','reference Rentas'),
                Field('monto','double'),
                singular='Transacción',plural='Transacciones',
                )


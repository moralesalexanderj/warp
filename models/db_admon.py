# -*- coding: utf-8 -*-
db.define_table('Contactos_tipo',
                Field('tipo','string'),
                format='%(tipo)s',
                )
db.define_table('Contactos',
                Field('nombre','string'),
                Field('apellido','string'),
                Field('nombre_completo',compute=lambda r: r['nombre'] + r['apellido']),
                Field('tipo','list:reference Contactos_tipo'),
                format='%(nombre)s %(apellido)s',
                singular='Contacto',plural='Contactos',
               )




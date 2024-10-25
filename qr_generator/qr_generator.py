import os
import sys

import qrcode # type: ignore

def validate_args() -> tuple[str, str, str]:
    if len( sys.argv ) != 4:
        print('Ingrese los parámetros requeridos: data, nombre y destino')

    return sys.argv[1], sys.argv[2], sys.argv[3]

def exists_path( path: str ) -> bool:
    is_valid_path = True

    if os.path.exists( path ):

        if not os.path.isdir( path ):
            print(f'La ruta {path} no es un directorio válido')
            is_valid_path = False

        is_valid_path = True
    else:
        print(f'El directorio { path } no existe')
        is_valid_path = False

    return is_valid_path

def generate_qr_code( data: str, name: str, destination: str ) -> str:

    qr = qrcode.QRCode( version=2, box_size=10, border=4 )
    qr.add_data( data )
    qr.make( fit=True )

    image = qr.make_image( fill='tomato', back_color='white' )

    file_path = os.path.join(destination, f"{name}.png")

    image.save( file_path )

    return file_path

def has_qr_created( path: str ) -> bool:
    return os.path.exists( path )

def main():
    data, name, destination = validate_args()
    file_path: str = ''

    if exists_path( destination ):
        file_path = generate_qr_code( data, name, destination )

    if not has_qr_created( file_path ):
        print('Ocurrió un error, intenta nuevamente.')

    print('Success!!!')
    print(f'route: { file_path }')

main()

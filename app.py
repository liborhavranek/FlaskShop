""" Libor Havránek App Copyright (C)  23.3 2023 """

from myshop import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0',)

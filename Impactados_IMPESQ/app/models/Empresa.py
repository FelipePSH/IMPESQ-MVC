from models import mysql

conn = mysql.connect()
cursor = conn.cursor()


class Empresa:
    def __init__(self, cnpj, email, nomeEmpresa):
        self.cnpj = cnpj
        self.email = email
        self.nomeEmpresa = nomeEmpresa

    def insert(self, cnpj, email, nomeEmpresa):
        try:
            if email and cnpj and nomeEmpresa:
                cursor.execute(
                    'insert into tbl_objeto_pesquisa (empresa_nome, cnpj, email) VALUES (%s, %s, %s)',
                    (nomeEmpresa, cnpj, email))
                conn.commit()

        except:
            "Erro ao inserir no banco"

        def read():
            try:
                if email and cnpj and nomeEmpresa:
                    cursor.execute(
                        'select * from tbl_objeto_pesquisa')
                    conn.commit()

            except:
                "Erro ao inserir no banco"

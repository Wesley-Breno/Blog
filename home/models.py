from django.db import models


class Post(models.Model):
    titulo_topo = models.CharField(max_length=32)
    titulo = models.CharField(max_length=50)
    mini_descricao = models.CharField(max_length=120)
    conteudo_post = models.CharField(max_length=2000)
    url_foto = models.CharField(max_length=50000)
    total_curtidas = models.IntegerField(default=0)
    total_comentarios = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo_topo


class Comentarios(models.Model):
    nome = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=1000, blank=True, null=True)
    instagram = models.CharField(max_length=1000, blank=True, null=True)
    comentario = models.CharField(max_length=2000)
    mostrar = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comentario


class Curtidas(models.Model):
    ip_usuario = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post}'

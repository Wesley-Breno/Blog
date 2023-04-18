from django.shortcuts import render, redirect
from .models import Post, Comentarios, Curtidas
from django.contrib import messages


def home(request):
    dicionario = {}
    dicionario['posts'] = Post.objects.all()
    dicionario['comentarios'] = Comentarios.objects.all()
    dicionario['curtidas'] = Curtidas.objects.all()

    return render(request, 'home/home.html', dicionario)


def post(request, pk):
    if request.method != 'POST':
        dicionario = {}
        dicionario['posts'] = Post.objects.get(pk=pk)
        dicionario['comentarios'] = Comentarios.objects.all().filter(post=pk, mostrar=True)
        dicionario['curtidas'] = Curtidas.objects.all().filter(post=pk)
        return render(request, 'home/post.html', dicionario)

    nome_usuario = request.POST.get('nome_usuario')
    comentario_usuario = request.POST.get('comentario_usuario')
    linkedin_usuario = request.POST.get('linkedin_usuario')
    instagram_usuario = request.POST.get('instagram_usuario')

    post = Post.objects.get(pk=pk)

    if 3 <= len(nome_usuario) <= 100 and 1 < len(comentario_usuario) <= 2000:
        Comentarios.objects.create(
            nome=nome_usuario, comentario=comentario_usuario, linkedin=linkedin_usuario, instagram=instagram_usuario,
            post=post
        )
        messages.add_message(request, messages.SUCCESS, 'Obrigado por comentar! O comentario foi enviado para analise.')
    else:
        messages.add_message(request, messages.ERROR, 'Por favor, preencha os campos corretamente.')

    dicionario = {}
    dicionario['posts'] = Post.objects.get(pk=pk)
    dicionario['comentarios'] = Comentarios.objects.all().filter(post=pk)
    dicionario['curtidas'] = Curtidas.objects.all().filter(post=pk)
    return redirect(f'/{pk}')


def curtiu(request, pk):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    post = Post.objects.get(pk=pk)
    usuario_ja_curtiu = Curtidas.objects.all().filter(post=pk, ip_usuario=ip)
    if len(usuario_ja_curtiu) > 0:
        ...
    else:
        adicionar_curtida = Post.objects.get(id=pk)
        adicionar_curtida.total_curtidas += 1
        adicionar_curtida.save()

        messages.add_message(request, messages.SUCCESS, 'Obrigado por curtir o post!')

        salvar_usuario_que_curtiu = Curtidas.objects.create(ip_usuario=ip, post=post)

    return redirect(f'post/{pk}')

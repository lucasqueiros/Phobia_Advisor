import sys
from pytubefix import YouTube

url_video = "https://www.youtube.com/watch?v=DuvXmEaH_rI"

def baixar_video(url, proxies=None, use_oauth=False, allow_oauth_cache=True):
    # Instancia o objeto YouTube com callbacks e proxies
    yt = YouTube(
        url,
        on_progress_callback=progress_func,
        on_complete_callback=complete_func,
        proxies=proxies,
        use_oauth=use_oauth,
        allow_oauth_cache=allow_oauth_cache
    )

    # Seleciona o stream de maior resolução
    ys = yt.streams.get_highest_resolution()

    # Faz o download para o diretório 'data'
    output_path = 'data'
    ys.download(output_path=output_path, filename='video')

    # Retorna o caminho completo do arquivo baixado
    return f'{output_path}/{ys.default_filename}'

def progress_func(stream, chunk, bytes_remaining):
    total_size = stream.filesize  # Tamanho total do vídeo
    bytes_downloaded = total_size - bytes_remaining  # Quantidade já baixada
    percentage_of_completion = (bytes_downloaded / total_size) * 100  # Porcentagem concluída

    # Atualizando a barra de progresso
    progress_bar_length = 50  # Tamanho da barra de progresso no terminal
    completed_length = int(progress_bar_length * bytes_downloaded // total_size)
    bar = '█' * completed_length + '-' * (progress_bar_length - completed_length)

    # Print da barra de progresso e porcentagem
    sys.stdout.write(f'\r|{bar}| {percentage_of_completion:.2f}% Complete')
    sys.stdout.flush()


def complete_func(stream, file_path):
    print(f'\nDownload completo! O arquivo foi salvo em: {file_path}')
    # Aqui você pode adicionar o que quiser fazer após o download, como processar o vídeo

baixar_video(url_video)
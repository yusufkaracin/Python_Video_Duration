def get_duration(file_name):
    """
    you should install ffmpeg.
    tested mp4, flv and 3gp.
    http://stackoverflow.com/questions/3844430/how-to-get-video-duration-in-python-or-django
    :param file_name:
    :return:
    """
    from subprocess import Popen, PIPE, STDOUT
    from math import ceil

    command = (
        'ffprobe',
        "-v", "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        file_name
    )

    try:
        with Popen(command, stdout=PIPE, stderr=STDOUT) as result:
            duration = float(result.stdout.readlines()[0].strip().decode("UTF-8"))
        return ceil(duration)
    except:
        return 0

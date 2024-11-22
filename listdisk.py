from winsys._kernel32 import FindFirstVolume, FindNextVolume


def get_volumes() -> list[str]:
    handle, first = FindFirstVolume()
    volumes = [first]

    while (volume := FindNextVolume(handle)) and isinstance(volume, str):
        volumes.append(volume)

    return volumes

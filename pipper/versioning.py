import semver


def serialize(version: str) -> str:
    """ """

    try:
        info = semver.parse_version_info(version)
    except ValueError:
        raise ValueError('Invalid semantic version "{}"'.format(version))

    pre = info.prerelease.replace('.', '_') if info.prerelease else None
    build = info.build.replace('.', '_') if info.build else None

    return 'v{}-{}-{}{}{}'.format(
        info.major,
        info.minor,
        info.patch,
        '-p-{}'.format(pre) if pre else '',
        '-b-{}'.format(build) if build else ''
    )


def deserialize(version: str) -> str:
    """ """

    return (
        version
        .lstrip('v')
        .replace('-', '.', 2)
        .replace('-p-', '-')
        .replace('-b-', '+')
    )
from invoke import Context, task


def run(ctx: Context, cmd: str):
    ctx.run(f"docker compose run --rm --no-deps backend {cmd}", pty=True)


@task
def up(ctx: Context):
    ctx.run("docker compose up -d --remove-orphans", pty=True)


@task
def down(ctx: Context, v: bool = False) -> None:
    """
    Shorthand for docker-compose down.
    Pass -v to remove named and anonymous volumes attached to the compose containers.
    """
    ctx.run(f"docker compose down {'--volumes' * v}", pty=True)


@task
def bash(ctx: Context):
    run(ctx, "bash")


@task
def logs(ctx: Context, service: str = "backend"):
    ctx.run(f"docker compose logs -f {service}", pty=True)


@task
def shell(ctx: Context):
    run(ctx, "python manage.py shell")


@task
def makemigrations(ctx: Context):
    run(ctx, "python manage.py makemigrations")


@task
def migrate(ctx: Context):
    run(ctx, "python manage.py migrate")

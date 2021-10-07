FROM public.ecr.aws/lambda/python:3.8

WORKDIR /opt/translate

# Install Pipenv
RUN python3 -m pip install pipenv

# Install Script Deps
COPY --chmod=0444 Pipfile Pipfile.lock /opt/
RUN cd /opt && pipenv sync --system

# Copy script code
USER 993:990
COPY --chmod=0775 . $WORKDIR

USER root
ENTRYPOINT ["python", "scripts/translate.py"]

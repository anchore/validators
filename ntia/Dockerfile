FROM python:3.13.1-alpine3.21

# Install the required package
RUN pip install ntia-conformance-checker

# Copy the wrapper script into the container
COPY ./wrapper.py /usr/local/bin/wrapper.py

# Make sure wrapper.py is executable
RUN chmod +x /usr/local/bin/wrapper.py

# Set the entrypoint so we can pass arguments when running the container
ENTRYPOINT ["python3", "/usr/local/bin/wrapper.py"]

FROM python:alpine3.17

RUN pip install httpserver
RUN pip install websockets

COPY --chown=root:root test.py /root/test.py
COPY --chown=root:root test2.py /root/test2.py
COPY --chown=root:root test.sh /root/test.sh


#CMD ["python", "/root/test.py", "&", "python", "/root/test2.py"]
CMD ["/root/test.sh"]

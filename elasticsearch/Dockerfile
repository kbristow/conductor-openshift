FROM elasticsearch:2.4
USER root
RUN chgrp -R 0 /usr/share/elasticsearch && \
    chmod -Rf g+rwx /usr/share/elasticsearch
USER elasticsearch
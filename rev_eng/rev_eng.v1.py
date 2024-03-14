import logging

from bitcoin import *


logger = logging.getLogger(__name__)
logging.basicConfig(format='%(message)s', level=logging.INFO)
logger.setLevel(logging.INFO)

priv = sha256('some big long brainwallet password')
logger.info("Priv: {}".format(priv))


logger.info("=========================================================================================================")

logger.info("Private to Public Key")
logger.info("---------------------")
pub = privtopub(priv) # <- What is encoding?
logger.info("Pub: {}".format(pub))

logger.info("=========================================================================================================")

logger.info("Public to Address")
logger.info("---------------------")
addr = pubtoaddr(pub)
logger.info("Addr: {}".format(addr))

logger.info("=========================================================================================================")

logger.info("Address History (Previous Transaction Outputs)")
logger.info("---------------------")
h = history(addr)
logger.info("Addr History: {}".format(h))

logger.info("=========================================================================================================")

logger.info("User Defined Output")
logger.info("---------------------")
outs = [{'value': 90000, 'address': '16iw1MQ1sy1DtRPYw3ao1bCamoyBJtRB4t'}]
logger.info("Outs: {}".format(outs))

logger.info("=========================================================================================================")

logger.info("Create Transaction")
logger.info("---------------------")
tx = mktx(h,outs) # <- CRITICAL TO UNDERSTAND
logger.info("Tx: {}".format(tx))

logger.info("=========================================================================================================")

tx2 = sign(tx,0,priv)
logger.info("Tx2: {}".format(tx2))

tx3 = sign(tx2,1,priv)
logger.info("Tx3: {}".format(tx3))

# pushtx(tx3)

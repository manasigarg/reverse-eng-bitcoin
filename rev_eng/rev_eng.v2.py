import logging

from bitcoin import *


logger = logging.getLogger(__name__)
logging.basicConfig(format='%(message)s', level=logging.INFO)
logger.setLevel(logging.INFO)

priv = "0CAECF01D74102A28AED6A64DCF1CF7B0E41C4DD6C62F70F46FEBDC32514F0BD"#sha256('some big long brainwallet password')
logger.info("Priv: {}".format(priv))

addr = "1MMMMSUb1piy2ufrSguNUdFmAcvqrQF8M5"
logger.info("Address History (Previous Transaction Outputs)")
logger.info("---------------------")
h = history(addr)
logger.info("Addr History: {}".format(h))

logger.info("=========================================================================================================")

logger.info("User Defined Output")
logger.info("---------------------")
outs = [{'value': 91234, 'address': '1KKKK6N21XKo48zWKuQKXdvSsCf95ibHFa'}]
logger.info("Outs: {}".format(outs))

logger.info("=========================================================================================================")

logger.info("Create Transaction")
logger.info("---------------------")
tx = mktx(h,outs) # <- CRITICAL TO UNDERSTAND
logger.info("Tx: {}".format(tx))

tx2 = sign(tx,0,priv)
logger.info("Tx2: {}".format(tx2))


from cloudAMQP_client import CloundAMQPClient

CLOUDAMQP_URL = 'amqp://holajbod:izGGmsaUFTKfY1gOSSeTN8N466Yi6_1C@crane.rmq.cloudamqp.com/holajbod'
TEST_QUEUE_NAME = 'test'

def test_basic():
    client = CloundAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sentMsg = {'test':'123'}
    client.sendMessage(sentMsg)
    receivedMsg = client.getMessage()

    assert sentMsg == receivedMsg
    print "test_basic passed."

if __name__ == '__main__':
    test_basic()
#ip는 주소를 나타냅니다. IPv4또는 IPv6 등으로 표현되면 숫자로 표현된 접속주소라고 생각하면 됩니다.
'''
여기서 내부IP와 외부 IP의 차이점은 집주소를 아파트로 본다면 외부 IP는 XX시 XX동 XX아파트 입니다. 
아파트까지 주소를 찾아왔다면 동 호수를 알아야 정확한 집주소를 찾을 수 있습니다. 
내부 IP는 동 호수로 볼 수 있습니다.
일반적으로 인터넷 망이 설치된 가정집에는 공유기가 있어 여러 대의 컴퓨터, 스마트폰, TV등의 기기를 연결하여 사용합니다.
내부IP는 집에 있는 공유기가 주소를 할당하여 줍니다.
하지만 외부 IP는 KT,LG 등 인터넷 망 공급자가 주소를 할당하여 줍니다. 
우리는 내부 및 외부 IP를 확인하여 정확하게 자신의 컴퓨터가 연결된 주소를 알 수 있습니다.
'''

#다음코드로 컴퓨터 내부IP를 알아봅시다.
import socket#컴퓨터가 연결된 접속 정보를 받아올 때 사용하는 모듈을 불러옵니다.
in_addr= socket.gethostbyname(socket.gethostname()) #연결된 소켓의 이름을 가져와 in_addr 변수와 바인딩합니다.
print(in_addr)#in_addr을 출력하여 내부 IP를 확인합니다.

import sys

def ip_to_decimal(ip):
    return sum(int(octet) * (256 ** (3 - i)) for i, octet in enumerate(ip.split(".")))

def decimal_to_ip(decimal):
    return ".".join(str((decimal >> (8 * i)) & 0xFF) for i in range(3, -1, -1))

def decimal_to_binary_string(decimal):
    return bin(decimal)[2:].zfill(32)  # 32비트 이진수 문자열로 변환

def get_subnet_mask(ip, subnet=None):
    if subnet is not None:
        # /25와 같은 형태일 경우
        mask = (1 << 32) - (1 << (32 - subnet))
    else:
        # 클래스 기반 서브넷 마스크
        first_octet = int(ip.split(".")[0])
        if first_octet < 128:
            mask = 0xFF000000  # Class A
        elif first_octet < 192:
            mask = 0xFFFF0000  # Class B
        else:
            mask = 0xFFFFFF00  # Class C

    return mask

def main():
    userInput = sys.stdin.readline().strip()

    if "/" in userInput:
        # /가 있는 경우
        ip_part, subnet_part = userInput.split("/")
        subnet = int(subnet_part)
        ip = ip_part
    else:
        # /가 없는 경우
        ip = userInput
        subnet = None

    subnet_mask = get_subnet_mask(ip, subnet)
    ip_decimal = ip_to_decimal(ip)
    
    # AND 연산
    network_address_decimal = ip_decimal & subnet_mask

    # 결과를 10진수 IP 형식으로 변환
    network_address_ip = decimal_to_ip(network_address_decimal)

    # 서브넷 마스크의 이진수 표현
    subnet_mask_binary = decimal_to_binary_string(subnet_mask)

    print("서브넷 마스크:", decimal_to_ip(subnet_mask))
    print("서브넷 마스크 (이진수):", subnet_mask_binary)
    print("네트워크 주소:", network_address_ip)

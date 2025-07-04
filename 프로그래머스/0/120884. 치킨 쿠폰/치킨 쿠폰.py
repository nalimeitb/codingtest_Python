def solution(chicken):
    
    answer = chicken // 10
    coupon_chicken = 0 # 남은 쿠폰의 수
    
    remain = chicken % 10 #최초 시켜먹은 치킨 쿠폰들에서 서비스치킨으로 바뀌지 못한 쿠폰들
    coupon_chicken = remain + (chicken // 10)
    
    while coupon_chicken >= 10 :
        answer = answer + (coupon_chicken // 10)
        coupon_chicken = coupon_chicken // 10 + coupon_chicken % 10
    
    
    # tmp = chicken
    # sum1 = 0
    
#     while True :
#         tmp = tmp // 10
#         print(tmp)
#         sum1 = sum1 + tmp
#         print(sum1)
#         if tmp < 10 :
#             break
    
#     answer = sum1
    
#         service = service + remain
#         service = service // 10
#         answer = answer + service
        
#     chicken + chicken // 10 + (chicken // 10)
    
    # 1081
    #  108
    #   10
    #    1
    # 1200

    
    # coupon = chicken #치킨 개수 1081마리, 쿠폰 1081개 1081 + 108 + 10 + 1
    # service1 = chicken // 10 #1차 서비스 108마리
    # remain_coupon1 = chicken % 10 #1차 서비스 치킨 구매 후 남은 쿠폰 개수 1개
    # service_coupon2 = service // 10 #2차 서비스 10마리, 쿠폰 남은거 8개
    # remain_coupon2 = service_coupon2 % 10
    # remain_coupon = remain_coupon + 
    
    return answer
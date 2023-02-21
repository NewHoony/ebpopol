var swiper = new Swiper(".mySwiper", {
    direction: "vertical", //슬라이드 수직 정렬
    slidesPerView: 1,      //한번에 보여줄 슬라이드 개수
    spaceBetween: 0,       //슬라이드 사이 여백
    mousewheel: true,      // 마우스 휠로 내리기
    pagination: {          
      el: ".swiper-pagination", // 페이지 이동 버튼을 담을 태그
      clickable: true,          // 페이지 이동 버튼 클릭 가능 여부
    },
    navigation: {
        prevEl: '.promotion .swiper-prev', // 이전 요소
        nextEl: '.promotion .swiper-next', // 다음 요소
        }
  });



var posts=["2024/07/26/我的博客会越来越好的/","2024/07/24/这是我的第一篇博客文章/","2024/07/24/论Python/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };
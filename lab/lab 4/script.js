const form = document.getElementById('loginForm');
const cancelBtn = document.querySelector('.cancel');

form.addEventListener('submit', function(e){
  e.preventDefault();
  const username = document.getElementById('username').value.trim();
  const password = document.getElementById('password').value.trim();
  if(username === '' || password === ''){
    alert('Vui lòng nhập đầy đủ thông tin');
    return;
  }
  alert('Đăng nhập thành công (demo)');
});

// Nút X (Cancel) reset form
cancelBtn.addEventListener('click', function(){
  form.reset();
});

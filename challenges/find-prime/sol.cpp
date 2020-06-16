bool isPrime(int num) {
  if (num <= 1) return false;
  std::cout << num;
  bool is_prime = true;
  for(int i = 2; i*i <= num; i++) {
    if(num % i == 0) {
    is_prime = false;
    break;
    }
  }
  return is_prime;
}
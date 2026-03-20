import json
import time
import requests

BASE_URL = "http://localhost:8888"
REQUEST_TIMEOUT = 10

def test_root():
    #Test root endpoint
    response = requests.get(f"{BASE_URL}/", timeout=REQUEST_TIMEOUT)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200

def test_health():
    # Test health endpoint
    response = requests.get(f"{BASE_URL}/health", timeout=REQUEST_TIMEOUT)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200

def test_predict():
    #Test predict endpoint
    test_data = {"features": [1.5, 2.3, 3.7]}
    print(f"Request: {json.dumps(test_data, indent=2)}")

    response = requests.post(
        f"{BASE_URL}/api/v1/predict",
        json=test_data,
        timeout=REQUEST_TIMEOUT,
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200

def test_predict_multiple():
    # Multiple requests for metrics generation
    test_cases = [
        [1.0, 2.0, 3.0],
        [0.5, 1.5, 2.5],
        [2.0, 3.0, 4.0],
        [1.5, 2.5, 3.5],
        [0.8, 1.8, 2.8],
    ]

    results = []
    for i, features in enumerate(test_cases, 1):
        try:
            response = requests.post(
                f"{BASE_URL}/api/v1/predict",
                json={"features": features},
                timeout=REQUEST_TIMEOUT,
            )
            response.raise_for_status()
            payload = response.json()
            prediction = payload.get("prediction")
            if prediction is None:
                raise KeyError("prediction is missing in response")
            results.append(payload)
            print(f"Request {i}: {features} -> {prediction:.2f}")
            time.sleep(0.5)
        except requests.exceptions.RequestException as e:
            print(f"Request error in request {i}: {e}")
        except (ValueError, KeyError, TypeError) as e:
            print(f"Response parsing error in request {i}: {e}")

    return len(results) == len(test_cases)

def test_logs():
    # Test logs retrieval from DB
    response = requests.get(f"{BASE_URL}/api/v1/logs?limit=5", timeout=REQUEST_TIMEOUT)
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Logs count: {data['count']}")
    if data['count'] > 0:
        print(f"Latest log: {json.dumps(data['logs'][0], indent=2)}")
    return response.status_code == 200

def test_metrics():
    # Test metrics endpoint
    response = requests.get(f"{BASE_URL}/metrics", timeout=REQUEST_TIMEOUT)
    print(f"Status: {response.status_code}")

    # Парсим метрики
    lines = response.text.split('\n')
    metrics = [line for line in lines if line and not line.startswith('#')]
    print(f"Metrics found: {len(metrics)}")
    print("\nMetrics examples:")
    for metric in metrics[:5]:
        print(f"  {metric}")

    return response.status_code == 200

def main():
    # Run all API checks

    tests = [
        ("Root endpoint", test_root),
        ("Health endpoint", test_health),
        ("Predict endpoint", test_predict),
        ("Multiple predictions", test_predict_multiple),
        ("Logs endpoint", test_logs),
        ("Metrics endpoint", test_metrics),
    ]

    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except requests.exceptions.ConnectionError:
            print(f"\nERROR: Could not connect to {BASE_URL}")
            print("Make sure ML service is running: make up-ml-service")
            return
        except Exception as e:
            print(f"\nERROR in test '{name}': {e}")
            results.append((name, False))

    # Итоги
    for name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"{status} - {name}")

    passed = sum(1 for _, result in results if result)
    total = len(results)
    print(f"\nSummary: {passed}/{total} tests passed")

    if passed == total:
        print("\nAll tests passed successfully!")
    else:
        print("\nSome tests failed. Check logs for details.")

if __name__ == "__main__":
    main()
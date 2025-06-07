import json

def find_incorrect_scores(data):
    incorrect_users = []
    
    for user in data:
        username = user['username']
        reported_score = user['score']
        actual_score = sum(value for key, value in user.items() 
                         if key not in ['username', 'score'])
        
        if actual_score != reported_score:
            incorrect_users.append(username)
    
    return sorted(incorrect_users)

def main():
    try:
        with open('test_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        result = find_incorrect_scores(data)
        
        for username in result:
            print(username)
            
    except FileNotFoundError:
        sys.exit(1)
    except json.JSONDecodeError:
        sys.exit(1)

if __name__ == "__main__":
    import sys
    main()
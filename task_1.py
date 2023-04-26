import requests


def get_activity_suggestions(num_activities):
    activities = []
    for i in range(num_activities):
        response = requests.get('https://www.boredapi.com/api/activity')
        activity_data = response.json()
        activity = {
            'key': i+1,
            'type': activity_data['type'],
            'activity': activity_data['activity'],
            'participants': activity_data['participants'],
            'price': activity_data['price'],
            'link': activity_data['link'],
            'accessibility': activity_data['accessibility']
        }
        activities.append(activity)
    return activities


def generate_table(activities):
    # Create table header
    header = '| Key | Type | Activity | Participants | Price | Link | Accessibility |\n'
    header += '| --- | ---- | -------- | ------------ | ----- | ---- | -------------- |\n'

    # Create table rows
    rows = ''
    for activity in activities:
        rows += '| {} | {} | {} | {} | {} | {} | {} |\n'.format(
            activity['key'], activity['type'], activity['activity'],
            activity['participants'], activity['price'], activity['link'], activity['accessibility'])

    return header + rows


def generate_insights(activities):
    # Most Participants
    most_participants = max(activities, key=lambda x: x['participants'])
    most_participants_text = 'Most Participants: {} (participants: {})\n'.format(
        most_participants['activity'], most_participants['participants'])

    # Duplicate Activities
    activity_names = [activity['activity'] for activity in activities]
    duplicate_activities = set([x for x in activity_names if activity_names.count(x) > 1])
    if duplicate_activities:
        duplicate_activities_text = 'Duplicate Activities: {}\n'.format('\n'.join(duplicate_activities))
    else:
        duplicate_activities_text = 'Duplicate Activities: -\n'

    # Most Characters in Activity
    most_characters = max(activities, key=lambda x: len(x['activity']))
    most_characters_text = 'Most characters in Activity: {} (characters: {})\n'.format(
        most_characters['activity'], len(most_characters['activity']))

    return most_participants_text + duplicate_activities_text + most_characters_text


def generate_markdown_file(num_activities):
    activities = get_activity_suggestions(num_activities)

    # Create Markdown content
    markdown_content = generate_table(activities) + '\n' + generate_insights(activities)

    # Write Markdown file
    with open('activity_suggestions.md', 'w') as f:
        f.write(markdown_content)
        # 'w' stands for write

# Prompt with activity suggestions
activity_prompt = int(input("Choose a number between 1-100?"))

if activity_prompt < 1 or activity_prompt > 100:
    print("Invalid parameter")
    exit(0)

generate_markdown_file(activity_prompt)
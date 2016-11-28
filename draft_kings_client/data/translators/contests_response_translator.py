from draft_kings_client.data.translators.contest_response_translator import ContestResponseTranslator


class ContestsResponseTranslator:

    def __init__(self):
        pass

    @staticmethod
    def translate(response):
        if 'SelectedSport' not in response:
            raise KeyError('Missing SelectedSport field')

        if 'Contests' not in response:
            raise KeyError('Missing Contests field')

        if 'DraftGroups' not in response:
            raise KeyError('Missing DraftGroups field')

        contests = []
        for contest in response['Contests']:
            contests.append(ContestResponseTranslator.translate(response=contest))

        return contests

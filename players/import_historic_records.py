import csv
from players.models import HistoricRecord

def run():
    print("Iniciando a importação dos dados históricos...")  # Confirmar que o script foi chamado
    with open('C:\\Users\\Caio\\Downloads\\historicrecords.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            HistoricRecord.objects.create(
                school=row['School'],
                player=row['Player'],
                year_start=int(row['Year Start']) if row['Year Start'] else None,
                year_end=int(row['Year End']) if row['Year End'] else None,
                completions=int(row['Completions']) if row['Completions'] else None,
                attempts=int(row['Attempts']) if row['Attempts'] else None,
                completion_percentage=float(row['Completion% (min 300 att)'].replace('%', '').strip()) if row['Completion% (min 300 att)'] else None,
                yards=int(row['Yards']) if row['Yards'] else None,
                yards_per_attempt=float(row['Yards/Att']) if row['Yards/Att'] else None,
                touchdowns=float(row['TD']) if row['TD'] else None,
                interceptions=float(row['INT']) if row['INT'] else None,
                passer_rating=float(row['Passer Rating']) if row['Passer Rating'] else None,
                rush_attempts=float(row['Rush Att']) if row['Rush Att'] else None,
                rush_yards=int(row['Rush Yds']) if row['Rush Yds'] else None,
                yards_per_carry=float(row['Yards per carry']) if row['Yards per carry'] else None,
                rush_tds=float(row['Rush TDs']) if row['Rush TDs'] else None,
                receptions=int(row['Receptions']) if row['Receptions'] else None,
                receiving_yards=int(row['Receiving Yds']) if row['Receiving Yds'] else None,
                yards_per_catch=float(row['Yds/Catch']) if row['Yds/Catch'] else None,
                receiving_tds=int(row['Rec TDs']) if row['Rec TDs'] else None,
                plays_from_scrim=int(row['Plays from Scrim']) if row['Plays from Scrim'] else None,
                yards_from_scrim=int(row['Yds form Scrim']) if row['Yds form Scrim'] else None,
                avg_yards_per_play=float(row['Avg Yds/Play']) if row['Avg Yds/Play'] else None,
                scrimmage_tds=int(row['Scrimmage TDs']) if row['Scrimmage TDs'] else None,
            )
    print("Importação concluída!")  # Confirmar que a importação foi concluída

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sqlalchemy import create_engine

# Set seed for consistency
np.random.seed(42)

# --- 1. ALL 16 REGIONS OF GHANA ---
ghana_regions = [
    'Greater Accra', 'Ashanti', 'Western', 'Central', 'Eastern', 
    'Volta', 'Northern', 'Upper East', 'Upper West', 'Bono', 
    'Bono East', 'Ahafo', 'Savannah', 'North East', 'Oti', 'Western North'
]

tech_types = ['4G', '5G', 'Fiber']
statuses = ['Active', 'Active', 'Active', 'Maintenance']

# Generate 100 Base Stations across all 16 regions
stations_data = []
for i in range(1, 101):
    station_id = f"BST_{i:03d}"
    region_assigned = ghana_regions[i % 16] # Even distribution across all 16
    stations_data.append({
        'station_id': station_id,
        'station_name': f"Tower_{region_assigned.replace(' ', '')}_{i}",
        'region': region_assigned,
        'technology_type': np.random.choice(tech_types, p=[0.5, 0.3, 0.2]),
        'capacity_gbps': round(np.random.uniform(1.0, 10.0), 2),
        'status': np.random.choice(statuses)
    })
df_stations = pd.DataFrame(stations_data)

# --- 2. GENERATE DAILY PERFORMANCE LOGS (1 YEAR) ---
start_date = datetime(2025, 8, 1)
end_date = datetime(2026, 7, 31)
delta = end_date - start_date

days_range = delta.days + 1
performance_data = []

for day in range(days_range):
    current_date = start_date + timedelta(days=day)
    # Festive periods like December holidays or Easter
    is_festive = current_date.month == 12 or (current_date.month == 4 and 2 <= current_date.day <= 6)
    
    for station in stations_data:
        base_calls = np.random.randint(20000, 80000)
        total_calls = int(base_calls * 1.35) if is_festive else base_calls
        
        is_anomaly = np.random.rand() > 0.96
        drop_rate = np.random.uniform(0.02, 0.05) if is_anomaly else np.random.uniform(0.002, 0.012)
        
        dropped_calls = int(total_calls * drop_rate)
        
        traffic_multiplier = 1.4 if is_festive else (1.2 if is_anomaly else 1.0)
        traffic_gb = round(np.random.uniform(1500.0, 5000.0) * traffic_multiplier, 2)
        
        performance_data.append({
            'station_id': station['station_id'],
            'log_timestamp': current_date.strftime('%Y-%m-%d'),
            'traffic_gb': traffic_gb,
            'dropped_calls': dropped_calls,
            'total_calls': total_calls
        })
df_performance = pd.DataFrame(performance_data)

# --- 3. GENERATE OUTAGE INCIDENTS ---
outage_data = []
root_causes = ['Hardware Failure', 'Power Grid Failure', 'Fiber Cut', 'Software Glitch']
severities = ['Critical', 'Major', 'Minor']

for incident_id in range(1, 2501):
    random_station = np.random.choice(df_stations['station_id'])
    random_day = np.random.randint(0, days_range)
    
    incident_date = start_date + timedelta(days=random_day)
    start_time = incident_date + timedelta(hours=np.random.randint(0, 23), minutes=np.random.randint(0, 59))
    duration_minutes = np.random.randint(15, 600)
    end_time = start_time + timedelta(minutes=duration_minutes)
    
    outage_data.append({
        'incident_id': incident_id,
        'station_id': random_station,
        'start_time': start_time,
        'end_time': end_time,
        'root_cause': np.random.choice(root_causes),
        'severity': np.random.choice(severities, p=[0.2, 0.5, 0.3])
    })
df_outages = pd.DataFrame(outage_data)

# --- 4. BULK UPLOAD TO MYSQL ---
engine = create_engine('mysql+pymysql://telecom_analyst:TelecomAnalytics2026!@localhost:3306/TelecomNetworkDB')

print("Uploading 100 Base Stations across 16 Regions...")
df_stations.to_sql('Base_Stations', con=engine, if_exists='append', index=False)

print("Uploading 36,500 Daily Performance Records...")
df_performance.to_sql('Performance_Logs', con=engine, if_exists='append', index=False)

print("Uploading Incident Logs...")
df_outages.to_sql('Outage_Incidents', con=engine, if_exists='append', index=False)

print("Done! Nationwide Ghanaian telecom dataset successfully deployed to MySQL.")
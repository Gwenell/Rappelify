from utils.settings import settings

en = {
    "add_reminder": "Add Reminder",
    "settings": "Settings",
    "reminder_description": "Reminder description",
    "days_of_week": "Days of the week",
    "days_of_week_list": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "recurrence": "Recurrence",
    "recurring": "Recurring",
    "every": "Every",
    "days": "Days",
    "weeks": "Weeks",
    "months": "Months",
    "language": "Language",
    "theme": "Theme",
    "english": "English",
    "french": "French",
    "dark": "Dark",
    "light": "Light",
    "custom": "Custom",
    "oled": "OLED (Mobile)",
    "primary_color": "Primary Color",
    "secondary_color": "Secondary Color",
    "sync_code": "Sync Code",
    "enter_sync_code": "Enter sync code",
    "reminder": "Reminder",
    "acknowledge": "Acknowledge",
    "later": "Later",
    "confirmation": "Confirmation",
    "confirm_acknowledge": "Are you sure you want to acknowledge this reminder?",
    "save": "Save",
    "cancel": "Cancel"
}

fr = {
    "add_reminder": "Ajouter un rappel",
    "settings": "Paramètres",
    "reminder_description": "Description du rappel",
    "days_of_week": "Jours de la semaine",
    "days_of_week_list": ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"],
    "recurrence": "Récurrence",
    "recurring": "Récurrent",
    "every": "Tous les",
    "days": "Jours",
    "weeks": "Semaines",
    "months": "Mois",
    "language": "Langue",
    "theme": "Thème",
    "english": "Anglais",
    "french": "Français",
    "dark": "Sombre",
    "light": "Clair",
    "custom": "Personnalisé",
    "oled": "OLED (Mobile)",
    "primary_color": "Couleur primaire",
    "secondary_color": "Couleur secondaire",
    "sync_code": "Code de synchronisation",
    "enter_sync_code": "Entrez le code de synchronisation",
    "reminder": "Rappel",
    "acknowledge": "Acquitter",
    "later": "Plus tard",
    "confirmation": "Confirmation",
    "confirm_acknowledge": "Êtes-vous sûr de vouloir acquitter ce rappel ?",
    "save": "Enregistrer",
    "cancel": "Annuler"
}

def get_translation(key):
    lang = settings.get('language', 'en')
    if lang == 'fr':
        return fr.get(key, key)
    return en.get(key, key)

_ = get_translation

def set_language(lang):
    settings.set('language', lang)
    global _
    _ = get_translation
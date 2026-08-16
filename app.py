
import streamlit as st
from PIL import Image
import pandas as pd

# AI_IA_ROTATION_V31_LOADER
# Rotation Engine V3.1 — independent read-only loader
try:
    import pickle as _aiia_pickle
    from pathlib import Path as _AIPath

    _AI_ROTATION_ENGINE_FILE = _AIPath(
        str(_AIPath(__file__).resolve().parent / "engine_snapshot.pkl")
    )

    if _AI_ROTATION_ENGINE_FILE.exists():

        with open(
            _AI_ROTATION_ENGINE_FILE,
            "rb"
        ) as _aiia_f:

            _aiia_engine_snapshot = _aiia_pickle.load(
                _aiia_f
            )

        rotation_v31_df = _aiia_engine_snapshot.get(
            "rotation_v31_df",
            pd.DataFrame()
        )

    else:
        rotation_v31_df = pd.DataFrame()

except Exception:
    rotation_v31_df = pd.DataFrame()
# AI_IA_ROTATION_V31_LOADER_END

import pickle
import os
import textwrap

_PAGE_ICON_PATH = str(
    _AIPath(__file__).resolve().parent
    / "assets"
    / "ai_ia_logo.png"
)

_PAGE_ICON = (
    Image.open(_PAGE_ICON_PATH)
    if os.path.exists(_PAGE_ICON_PATH)
    else "◆"
)



# ================================================================
# PAGE CONFIG
# ================================================================

st.set_page_config(
    page_title="My Investment AI",
    page_icon=_PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ================================================================
# DATA LOCATION
# ================================================================

APP_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

PORTFOLIO_FILE = os.path.join(
    APP_DIR,
    "portfolio.csv"
)

ENGINE_FILE = os.path.join(
    APP_DIR,
    "engine_snapshot.pkl"
)


LOGO_FILE = os.path.join(
    APP_DIR,
    "assets",
    "ai_ia_logo.png"
)

logo_image = (
    Image.open(LOGO_FILE)
    if os.path.exists(LOGO_FILE)
    else None
)


# ================================================================
# SESSION STATE
# ================================================================

if "theme" not in st.session_state:
    st.session_state.theme = "Eggshell"

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"


# ================================================================
# THEMES
# ================================================================

THEMES = {

    "Eggshell": {

        "background": "#F3EFE4",
        "card": "#FAF8F2",
        "card_alt": "#EEE8DB",

        "text": "#282724",
        "muted": "#6D695F",

        "accent": "#96754A",
        "accent_soft": "#C7AD82",

        "border": "#C7B896",
        "nav": "#E8E0D0",

        "positive": "#57745C",
        "warning": "#A97938",
        "negative": "#8B4E47",

        "font_body":
            "Arial, Helvetica, sans-serif",

        "font_heading":
            "Georgia, 'Times New Roman', serif"
    },


    "Natural": {

        "background": "#EAE8DE",
        "card": "#F4F2E9",
        "card_alt": "#DEE1D3",

        "text": "#2B332A",
        "muted": "#687065",

        "accent": "#5E7252",
        "accent_soft": "#9BA788",

        "border": "#A79E87",
        "nav": "#D7D8C7",

        "positive": "#476B50",
        "warning": "#9A7444",
        "negative": "#83564A",

        "font_body":
            "Arial, Helvetica, sans-serif",

        "font_heading":
            "Georgia, 'Times New Roman', serif"
    },


    "Future": {

        "background": "#171A1C",
        "card": "#222629",
        "card_alt": "#292F32",

        "text": "#E6E1D4",
        "muted": "#9B9A92",

        "accent": "#B58A52",
        "accent_soft": "#6D8F8A",

        "border": "#755C3D",
        "nav": "#1D2224",

        "positive": "#6C9A7B",
        "warning": "#C09455",
        "negative": "#A96057",

        "font_body":
            "Arial, Helvetica, sans-serif",

        "font_heading":
            "Georgia, 'Times New Roman', serif"
    }
}


theme = THEMES[
    st.session_state.theme
]


# ================================================================
# GLOBAL CSS
# ================================================================




st.markdown(
    '\n<style>\n\n/* ============================================================\n   AI | IA PORTFOLIO SUMMARY CARDS\n   ============================================================ */\n\n.aiia-metric-card {\n\n    min-height: 165px;\n\n    padding:\n        24px 24px 20px 24px;\n\n    background:\n        rgba(250,248,240,0.68);\n\n    border:\n        1px solid rgba(179,148,82,0.34);\n\n    border-top:\n        3px solid #344635;\n\n    border-radius:\n        4px 4px 18px 4px;\n\n    box-shadow:\n        0 4px 15px rgba(41,42,38,0.045);\n\n    text-align:\n        center;\n\n    position:\n        relative;\n\n}\n\n\n/* subtle Art-Deco corner detail */\n\n.aiia-metric-card::after {\n\n    content: "";\n\n    position:\n        absolute;\n\n    width:\n        18px;\n\n    height:\n        18px;\n\n    right:\n        8px;\n\n    bottom:\n        8px;\n\n    border-right:\n        1px solid rgba(179,148,82,0.55);\n\n    border-bottom:\n        1px solid rgba(179,148,82,0.55);\n\n}\n\n\n.aiia-metric-title {\n\n    font-family:\n        "Avenir Next",\n        "Century Gothic",\n        "Trebuchet MS",\n        sans-serif;\n\n    font-size:\n        0.82rem;\n\n    font-weight:\n        600;\n\n    letter-spacing:\n        1.8px;\n\n    text-transform:\n        uppercase;\n\n    color:\n        #5D7057;\n\n    margin-bottom:\n        16px;\n\n}\n\n\n.aiia-metric-value {\n\n    font-family:\n        "Avenir Next",\n        "Century Gothic",\n        "Trebuchet MS",\n        sans-serif;\n\n    font-size:\n        2.05rem;\n\n    font-weight:\n        500;\n\n    letter-spacing:\n        0.4px;\n\n    color:\n        #292A26;\n\n    line-height:\n        1.15;\n\n}\n\n\n.aiia-metric-detail {\n\n    font-family:\n        "Avenir Next",\n        "Century Gothic",\n        "Trebuchet MS",\n        sans-serif;\n\n    font-size:\n        0.76rem;\n\n    letter-spacing:\n        0.5px;\n\n    color:\n        rgba(41,42,38,0.62);\n\n    margin-top:\n        13px;\n\n}\n\n\n/* restrained financial indicators */\n\n.metric-up {\n\n    color:\n        #3E6745;\n\n}\n\n.metric-down {\n\n    color:\n        #8A4741;\n\n}\n\n</style>\n',
    unsafe_allow_html=True
)

st.markdown(
    '\n<style>\n\n/* ============================================================\n   AI | IA PERMANENT BRAND SYSTEM\n   ============================================================ */\n\n:root {\n\n    --aiia-green: #344635;\n    --aiia-green-soft: #5D7057;\n\n    --aiia-gold: #B39452;\n    --aiia-gold-soft: #CCB77C;\n\n    --aiia-charcoal: #292A26;\n    --aiia-eggshell: #F1EEE3;\n\n}\n\n\n/* Navigation accent */\n\ndiv.stButton > button {\n\n    border-color:\n        rgba(179,148,82,0.48) !important;\n\n}\n\n\ndiv.stButton > button:hover {\n\n    border-color:\n        var(--aiia-gold) !important;\n\n    color:\n        var(--aiia-green) !important;\n\n    box-shadow:\n        0px 3px 12px\n        rgba(179,148,82,0.12);\n\n}\n\n\n/* Deco separators */\n\n.deco-rule::before,\n.deco-rule::after {\n\n    background:\n        rgba(179,148,82,0.55) !important;\n\n}\n\n.deco-diamond {\n\n    border-color:\n        var(--aiia-gold) !important;\n\n}\n\n\n/* Cards */\n\n.metric-card {\n\n    border-color:\n        rgba(179,148,82,0.32) !important;\n\n    border-top:\n        2px solid\n        var(--aiia-green-soft) !important;\n\n}\n\n\n/* Headings */\n\n.section-heading {\n\n    color:\n        var(--aiia-green) !important;\n\n}\n\n\n/* Brand logo block */\n\n.aiia-logo-wrap {\n\n    width: 100%;\n\n    display: flex;\n\n    justify-content: center;\n\n    align-items: center;\n\n    padding:\n        4px 0 12px 0;\n\n}\n\n</style>\n',
    unsafe_allow_html=True
)

st.markdown(
    '\n<style>\n\n/* ============================================================\n   EGGSHELL BUSINESS REPORT BACKGROUND\n   ============================================================ */\n\n[data-testid="stAppViewContainer"] {\n\n    background-color: #F1EEE3 !important;\n\n    background-image:\n\n        repeating-radial-gradient(\n            circle at 17% 32%,\n            rgba(70, 65, 48, 0.018) 0px,\n            rgba(70, 65, 48, 0.018) 1px,\n            transparent 1px,\n            transparent 4px\n        ),\n\n        linear-gradient(\n            115deg,\n            rgba(255,255,255,0.16),\n            rgba(211,205,184,0.07) 42%,\n            rgba(255,255,255,0.10) 70%,\n            rgba(188,181,157,0.05)\n        );\n\n    background-attachment: fixed;\n}\n\n\n/* Header blends into paper */\n\n[data-testid="stHeader"] {\n\n    background:\n        rgba(241,238,227,0.96) !important;\n}\n\n\n/* ============================================================\n   TYPOGRAPHY\n   ============================================================ */\n\nhtml, body,\n[data-testid="stAppViewContainer"],\n[data-testid="stAppViewContainer"] * {\n\n    font-family:\n        \'Avenir Next\',\n        \'Century Gothic\',\n        \'Trebuchet MS\',\n        Arial,\n        sans-serif !important;\n\n}\n\n\n/* ============================================================\n   ART-DECO NAVIGATION BUTTONS\n   ============================================================ */\n\ndiv.stButton > button {\n\n    min-height: 52px;\n\n    border-radius: 18px !important;\n\n    border:\n        1px solid\n        rgba(92,91,70,0.55) !important;\n\n    background:\n        rgba(250,248,240,0.38) !important;\n\n    font-size:\n        0.90rem !important;\n\n    font-weight:\n        500 !important;\n\n    letter-spacing:\n        1.4px !important;\n\n    text-transform: uppercase;\n\n    box-shadow:\n        0px 2px 8px\n        rgba(57,54,42,0.025);\n\n}\n\n\ndiv.stButton > button:hover {\n\n    background:\n        rgba(116,125,91,0.10) !important;\n\n    border-color:\n        rgba(76,98,67,0.85) !important;\n\n    transform:\n        translateY(-1px);\n\n}\n\n\n/* ============================================================\n   METRIC CARDS\n   ============================================================ */\n\n[data-testid="stMetric"] {\n\n    background:\n        rgba(250,248,240,0.72) !important;\n\n    border:\n        1px solid\n        rgba(92,91,70,0.28) !important;\n\n    border-top:\n        3px solid\n        rgba(76,98,67,0.90) !important;\n\n    border-radius:\n        3px !important;\n\n    padding:\n        22px 20px !important;\n\n    box-shadow:\n        0px 3px 12px\n        rgba(57,54,42,0.035);\n\n}\n\n\n/* ============================================================\n   DATA TABLES\n   ============================================================ */\n\n[data-testid="stDataFrame"] {\n\n    background:\n        rgba(250,248,240,0.60) !important;\n\n    border:\n        1px solid\n        rgba(92,91,70,0.22);\n\n}\n\n</style>\n',
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <style>

    /* --------------------------------
       MAIN APP
    -------------------------------- */

    .stApp {{
        background:
            {theme["background"]};
        color:
            {theme["text"]};
        font-family:
            {theme["font_body"]};
    }}


    /* --------------------------------
       REMOVE STREAMLIT DECORATION
    -------------------------------- */

    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    header {{
        background: transparent !important;
    }}


    /* --------------------------------
       MAIN WIDTH
    -------------------------------- */

    .block-container {{
        max-width: 1500px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
    }}


    /* --------------------------------
       BRAND HEADER
    -------------------------------- */

    .brand-shell {{
        text-align: center;
        padding:
            18px 20px 12px 20px;

        border-top:
            3px double {theme["accent"]};

        border-bottom:
            3px double {theme["accent"]};

        margin-bottom:
            18px;
    }}

    .brand-title {{
        font-family:
            {theme["font_heading"]};

        font-size:
            34px;

        letter-spacing:
            5px;

        color:
            {theme["text"]};

        margin: 0;
    }}

    .brand-subtitle {{
        font-size:
            11px;

        letter-spacing:
            4px;

        color:
            {theme["muted"]};

        margin-top:
            5px;
    }}


    /* --------------------------------
       ART DECO ACCENT
    -------------------------------- */

    .deco-rule {{
        display: flex;
        align-items: center;
        gap: 12px;
        margin:
            10px 0 18px 0;
    }}

    .deco-rule::before,
    .deco-rule::after {{
        content: "";
        height: 1px;
        flex: 1;
        background:
            {theme["border"]};
    }}

    .deco-diamond {{
        width: 9px;
        height: 9px;
        border:
            1px solid {theme["accent"]};
        transform:
            rotate(45deg);
    }}


    /* --------------------------------
       NAVIGATION BUTTONS
    -------------------------------- */

    div[data-testid="stHorizontalBlock"]
    div.stButton > button {{

        background:
            transparent;

        color:
            {theme["text"]};

        border:
            1px solid {theme["border"]};

        border-radius:
            2px;

        min-height:
            42px;

        font-weight:
            600;

        letter-spacing:
            0.3px;

        transition:
            all 0.15s ease;
    }}

    div[data-testid="stHorizontalBlock"]
    div.stButton > button:hover {{

        border-color:
            {theme["accent"]};

        color:
            {theme["accent"]};

        background:
            {theme["card"]};
    }}


    /* --------------------------------
       KPI CARDS
    -------------------------------- */

    .metric-card {{

        background:
            {theme["card"]};

        border:
            1px solid {theme["border"]};

        border-top:
            3px solid {theme["accent"]};

        padding:
            22px 20px;

        min-height:
            135px;

        text-align:
            center;

        box-shadow:
            0 3px 12px rgba(0,0,0,0.04);
    }}

    .metric-title {{

        color:
            {theme["muted"]};

        font-size:
            11px;

        font-weight:
            700;

        letter-spacing:
            1.8px;

        text-transform:
            uppercase;
    }}

    .metric-value {{

        color:
            {theme["text"]};

        font-family:
            {theme["font_heading"]};

        font-size:
            32px;

        margin-top:
            12px;
    }}

    .metric-detail {{

        color:
            {theme["muted"]};

        font-size:
            12px;

        margin-top:
            4px;
    }}


    /* --------------------------------
       SECTION CARDS
    -------------------------------- */

    .section-card {{

        background:
            {theme["card"]};

        border:
            1px solid {theme["border"]};

        padding:
            22px;

        margin-bottom:
            20px;

        box-shadow:
            0 3px 12px rgba(0,0,0,0.035);
    }}

    .section-heading {{

        font-family:
            {theme["font_heading"]};

        font-size:
            20px;

        color:
            {theme["text"]};

        letter-spacing:
            1px;

        margin-bottom:
            15px;
    }}


    /* --------------------------------
       BADGES
    -------------------------------- */

    .badge-great {{
        color:
            {theme["positive"]};

        border:
            1px solid {theme["positive"]};

        padding:
            3px 7px;
    }}

    .badge-watch {{
        color:
            {theme["warning"]};

        border:
            1px solid {theme["warning"]};

        padding:
            3px 7px;
    }}

    .badge-review {{
        color:
            {theme["negative"]};

        border:
            1px solid {theme["negative"]};

        padding:
            3px 7px;
    }}


    /* --------------------------------
       TABLES
    -------------------------------- */

    [data-testid="stDataFrame"] {{
        border:
            1px solid {theme["border"]};
    }}


    /* --------------------------------
       SELECTBOX
    -------------------------------- */

    div[data-baseweb="select"] > div {{
        background:
            {theme["card"]};

        border-color:
            {theme["border"]};

        color:
            {theme["text"]};
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ================================================================
# INVESTMENT ENGINE
# ================================================================

@st.cache_data(show_spinner=False)
def load_engine():

    if not os.path.exists(ENGINE_FILE):
        return {}

    try:

        with open(ENGINE_FILE, "rb") as f:
            return pickle.load(f)

    except Exception as e:

        st.error(
            f"Investment engine could not be loaded: {e}"
        )

        return {}


engine = load_engine()


def engine_df(name):

    obj = engine.get(name)

    if isinstance(obj, pd.DataFrame):
        return obj.copy()

    return pd.DataFrame()


# Core engine outputs

master_investment = engine_df(
    "master_investment_df"
)

top5_overall = engine_df(
    "dashboard_top5_overall"
)

top5_new = engine_df(
    "dashboard_top5_new"
)

buy_more = engine_df(
    "dashboard_buy_more"
)

top5_holdings = engine_df(
    "dashboard_top5_holdings"
)

review_holdings = engine_df(
    "dashboard_review"
)

sector_exposure = engine_df(
    "dashboard_sector_exposure"
)

broad_discovery = engine_df(
    "broad_discovery_df"
)

deep_discovery = engine_df(
    "deep_discovery_df"
)

investable_discovery = engine_df(
    "investable_discovery_df"
)

forward_holdings = engine_df(
    "forward_holding_df"
)

rotation_moves = engine_df(
    "best_opportunity_moves_df"
)

# Prefer Rotation Engine V3.1 when available.
# Fall back to the original actionable rotation data if needed.
if (
    isinstance(rotation_v31_df, pd.DataFrame)
    and not rotation_v31_df.empty
):
    actionable_rotation = rotation_v31_df.copy()
else:
    actionable_rotation = engine_df(
        "actionable_opportunity_df"
    )

final_actions = engine_df(
    "final_actions_df"
)


# ================================================================
# DISPLAY HELPERS
# ================================================================

def clean_table(df, max_rows=None):

    if df is None or df.empty:
        return pd.DataFrame()

    out = df.copy()

    # Remove internal/debug columns from app display
    hide_terms = [
        "_merge",
        "index"
    ]

    remove = []

    for col in out.columns:

        if str(col).lower() in hide_terms:
            remove.append(col)

    if remove:
        out = out.drop(
            columns=remove,
            errors="ignore"
        )

    if max_rows is not None:
        out = out.head(max_rows)

    return out


def first_existing_column(df, candidates):

    if df is None or df.empty:
        return None

    for candidate in candidates:

        if candidate in df.columns:
            return candidate

    return None


def find_ticker_column(df):

    return first_existing_column(
        df,
        [
            "App_Ticker",
            "Ticker",
            "ticker",
            "Symbol",
            "symbol"
        ]
    )


def find_score_column(df):

    return first_existing_column(
        df,
        [
            "Master_Score",
            "Master Score",
            "Final_Score",
            "Investment_Score",
            "Score",
            "score"
        ]
    )


def top_opportunity():

    source = top5_overall

    if source.empty:
        source = master_investment

    if source.empty:
        return "—", None

    ticker_col = find_ticker_column(source)
    score_col = find_score_column(source)

    ticker = (
        str(source.iloc[0][ticker_col])
        if ticker_col
        else "—"
    )

    score = None

    if score_col:

        try:
            score = float(
                source.iloc[0][score_col]
            )

        except:
            score = None

    return ticker, score


def show_engine_table(
    df,
    empty_message="No qualifying investments.",
    rows=None
):

    display_df = clean_table(
        df,
        rows
    )

    if display_df.empty:

        st.info(empty_message)
        return

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )



# ================================================================
# PORTFOLIO DATA
# ================================================================

def load_portfolio():

    if not os.path.exists(
        PORTFOLIO_FILE
    ):

        return pd.DataFrame()

    df = pd.read_csv(
        PORTFOLIO_FILE
    )

    if "Active" in df.columns:

        active = (
            df["Active"]
            .astype(str)
            .str.lower()
            .isin(
                ["true", "1", "yes"]
            )
        )

        df = df[
            active
        ].copy()

    return df


portfolio = load_portfolio()


# ================================================================
# PORTFOLIO GROWTH
# ================================================================

def calculate_portfolio_growth(df):

    """
    Calculate portfolio growth only when genuine
    cost-basis information is available.

    Returns:
        growth_percent,
        gain_loss_value,
        invested_value

    If cost basis is unavailable:
        None, None, None
    """

    if df is None or df.empty:
        return None, None, None


    value_col = detect_value_column(df)

    if value_col is None:
        return None, None, None


    cost_candidates = [

        "Cost_Basis_GBP",
        "Cost_Basis",

        "Total_Cost_GBP",
        "Total_Cost",

        "Invested_GBP",
        "Invested_Value",

        "Purchase_Value_GBP",
        "Original_Value_GBP"
    ]


    cost_col = None


    for candidate in cost_candidates:

        if candidate in df.columns:

            cost_col = candidate
            break


    if cost_col is None:

        return None, None, None


    current_values = pd.to_numeric(
        df[value_col],
        errors="coerce"
    ).fillna(0)


    invested_values = pd.to_numeric(
        df[cost_col],
        errors="coerce"
    ).fillna(0)


    current_total = float(
        current_values.sum()
    )


    invested_total = float(
        invested_values.sum()
    )


    if invested_total <= 0:

        return None, None, None


    gain_loss = (
        current_total
        - invested_total
    )


    growth_percent = (
        gain_loss
        / invested_total
        * 100
    )


    return (
        growth_percent,
        gain_loss,
        invested_total
    )



# ================================================================
# PORTFOLIO METRICS
# ================================================================

def detect_value_column(df):

    candidates = [

        "Value_GBP",
        "Value",
        "Current_Value",
        "Market_Value",
        "Holding_Value",
        "Position_Value"
    ]

    for col in candidates:

        if col in df.columns:
            return col

    for col in df.columns:

        if "value" in str(col).lower():
            return col

    return None


value_col = detect_value_column(
    portfolio
)


if (
    not portfolio.empty
    and value_col is not None
):

    portfolio[value_col] = pd.to_numeric(
        portfolio[value_col],
        errors="coerce"
    ).fillna(0)

    total_value = float(
        portfolio[value_col].sum()
    )

else:

    total_value = 0.0



# ================================================================
# LIVE PORTFOLIO SUMMARY VALUES
# ================================================================

portfolio_growth, portfolio_gain_loss, portfolio_invested = (
    calculate_portfolio_growth(
        portfolio
    )
)


if portfolio_growth is None:

    portfolio_growth_text = "—"
    portfolio_growth_detail = (
        "Cost basis required"
    )
    portfolio_growth_direction = None


else:

    portfolio_growth_text = (
        f"{portfolio_growth:+.2f}%"
    )

    portfolio_growth_detail = (
        f"{portfolio_gain_loss:+,.2f} GBP"
    )

    portfolio_growth_direction = (
        "up"
        if portfolio_growth >= 0
        else "down"
    )


# Temporary until cost-basis tracking is connected
portfolio_growth = None





# ================================================================
# PORTFOLIO GROWTH
# ================================================================

def calculate_portfolio_growth(df):

    """
    Returns:
        growth_percent,
        gain_loss_value,
        invested_value

    Uses real cost-basis data only.
    Returns None values when sufficient data is unavailable.
    """

    if df is None or df.empty:
        return None, None, None


    value_col = detect_value_column(df)

    if value_col is None:
        return None, None, None


    cost_candidates = [

        "Cost_Basis_GBP",
        "Cost_Basis",
        "Total_Cost_GBP",
        "Total_Cost",
        "Invested_GBP",
        "Invested_Value",
        "Purchase_Value_GBP",
        "Original_Value_GBP"
    ]


    cost_col = None

    for candidate in cost_candidates:

        if candidate in df.columns:

            cost_col = candidate
            break


    if cost_col is None:

        return None, None, None


    current_values = pd.to_numeric(
        df[value_col],
        errors="coerce"
    ).fillna(0)


    invested_values = pd.to_numeric(
        df[cost_col],
        errors="coerce"
    ).fillna(0)


    current_total = float(
        current_values.sum()
    )

    invested_total = float(
        invested_values.sum()
    )


    if invested_total <= 0:

        return None, None, None


    gain_loss = (
        current_total
        - invested_total
    )


    growth_percent = (
        gain_loss
        / invested_total
        * 100
    )


    return (
        growth_percent,
        gain_loss,
        invested_total
    )


# ================================================================
# AI | IA METRIC CARD
# ================================================================

def aiia_metric_card(
    title,
    value,
    detail="",
    direction=None
):

    direction_class = ""

    if direction == "up":
        direction_class = "metric-up"

    elif direction == "down":
        direction_class = "metric-down"

    card_html = f"""
    <div class="aiia-metric-card">

        <div class="aiia-metric-title">
            {title}
        </div>

        <div class="aiia-metric-value {direction_class}">
            {value}
        </div>

        <div class="aiia-metric-detail">
            {detail}
        </div>

    </div>
    """

    st.html(
        textwrap.dedent(card_html).strip()
    )


# ================================================================
# BRAND
# ================================================================

if logo_image is not None:

    left_logo, centre_logo, right_logo = st.columns(
        [1.35, 1, 1.35]
    )

    with centre_logo:

        st.image(
            logo_image,
            use_container_width=True
        )

else:

    st.markdown(
        """
        <div class="brand-shell">

            <div class="brand-title">
                AI | IA
            </div>

            <div class="brand-subtitle">
                MY INVESTMENT AI
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ================================================================
# NAVIGATION
# ================================================================

nav_pages = [

    "Dashboard",
    "My Portfolio",
    "Top 5",
    "Discover",
    "Rotation",
    "Settings"
]


nav = st.columns(
    len(nav_pages)
)


for col, page in zip(
    nav,
    nav_pages
):

    with col:

        if st.button(
            page,
            use_container_width=True,
            key=f"nav_{page}"
        ):

            st.session_state.page = page
            st.rerun()


st.markdown(
    """
    <div class="deco-rule">
        <span class="deco-diamond"></span>
    </div>
    """,
    unsafe_allow_html=True
)


# ================================================================
# PORTFOLIO MANAGER
# ================================================================

PORTFOLIO_FILE = os.path.join(
    APP_DIR,
    "portfolio.csv"
)


def load_portfolio_database():

    if not os.path.exists(PORTFOLIO_FILE):
        return pd.DataFrame()

    return pd.read_csv(PORTFOLIO_FILE)


def save_portfolio_database(df):

    df.to_csv(
        PORTFOLIO_FILE,
        index=False
    )


def portfolio_ticker_column(df):

    candidates = [
        "Ticker",
        "ticker",
        "Symbol",
        "symbol",
        "App_Ticker"
    ]

    for col in candidates:

        if col in df.columns:
            return col

    return None


def portfolio_value_column(df):

    candidates = [
        "Value_GBP",
        "Portfolio_Value",
        "Value",
        "Current_Value",
        "Market_Value"
    ]

    for col in candidates:

        if col in df.columns:
            return col

    return None


def portfolio_active_column(df):

    candidates = [
        "Active",
        "active",
        "Currently_Held",
        "Held"
    ]

    for col in candidates:

        if col in df.columns:
            return col

    return None


# ================================================================
# ADD HOLDING
# ================================================================

def app_add_holding(
    ticker,
    value_gbp,
    sector=""
):

    df = load_portfolio_database()

    ticker_col = portfolio_ticker_column(df)
    value_col = portfolio_value_column(df)
    active_col = portfolio_active_column(df)

    ticker = str(ticker).strip().upper()

    if not ticker:
        return False, "Ticker required."

    if value_gbp <= 0:
        return False, "Holding value must be greater than zero."

    if ticker_col is None:
        return False, "Portfolio ticker column not found."

    if value_col is None:
        return False, "Portfolio value column not found."


    existing = (
        df[ticker_col]
        .astype(str)
        .str.upper()
        == ticker
    )


    if existing.any():

        row_index = df[existing].index[0]

        current_value = pd.to_numeric(
            df.loc[row_index, value_col],
            errors="coerce"
        )

        if pd.isna(current_value):
            current_value = 0

        df.loc[row_index, value_col] = (
            float(current_value)
            + float(value_gbp)
        )

        if active_col:
            df.loc[row_index, active_col] = True

        save_portfolio_database(df)

        return (
            True,
            f"{ticker} already existed. "
            f"Added £{value_gbp:,.2f} to the position."
        )


    new_row = {
        col: None
        for col in df.columns
    }

    new_row[ticker_col] = ticker
    new_row[value_col] = float(value_gbp)

    if active_col:
        new_row[active_col] = True


    sector_candidates = [
        "Sector",
        "sector",
        "Category"
    ]

    for col in sector_candidates:

        if col in df.columns:
            new_row[col] = sector
            break


    df = pd.concat(
        [
            df,
            pd.DataFrame([new_row])
        ],
        ignore_index=True
    )

    save_portfolio_database(df)

    return (
        True,
        f"{ticker} added to portfolio."
    )


# ================================================================
# BUY MORE
# ================================================================

def app_buy_more(
    ticker,
    additional_value
):

    df = load_portfolio_database()

    ticker_col = portfolio_ticker_column(df)
    value_col = portfolio_value_column(df)

    if ticker_col is None or value_col is None:
        return False, "Portfolio columns unavailable."

    ticker = str(ticker).strip().upper()

    mask = (
        df[ticker_col]
        .astype(str)
        .str.upper()
        == ticker
    )

    if not mask.any():
        return False, f"{ticker} is not currently in the portfolio."

    if additional_value <= 0:
        return False, "Amount must be greater than zero."

    idx = df[mask].index[0]

    old_value = pd.to_numeric(
        df.loc[idx, value_col],
        errors="coerce"
    )

    if pd.isna(old_value):
        old_value = 0

    df.loc[idx, value_col] = (
        float(old_value)
        + float(additional_value)
    )

    save_portfolio_database(df)

    return (
        True,
        f"Added £{additional_value:,.2f} to {ticker}."
    )


# ================================================================
# RECORD SALE
# ================================================================

def app_record_sale(
    ticker,
    sale_value
):

    df = load_portfolio_database()

    ticker_col = portfolio_ticker_column(df)
    value_col = portfolio_value_column(df)
    active_col = portfolio_active_column(df)

    if ticker_col is None or value_col is None:
        return False, "Portfolio columns unavailable."

    ticker = str(ticker).strip().upper()

    mask = (
        df[ticker_col]
        .astype(str)
        .str.upper()
        == ticker
    )

    if not mask.any():
        return False, f"{ticker} not found."

    idx = df[mask].index[0]

    current_value = pd.to_numeric(
        df.loc[idx, value_col],
        errors="coerce"
    )

    if pd.isna(current_value):
        current_value = 0

    sale_value = float(sale_value)

    if sale_value <= 0:
        return False, "Sale amount must be greater than zero."

    if sale_value >= current_value:

        df.loc[idx, value_col] = 0

        if active_col:
            df.loc[idx, active_col] = False

        message = (
            f"{ticker} marked as fully sold."
        )

    else:

        df.loc[idx, value_col] = (
            current_value - sale_value
        )

        message = (
            f"Recorded £{sale_value:,.2f} "
            f"sale from {ticker}."
        )


    save_portfolio_database(df)

    return True, message


# ================================================================
# EDIT HOLDING
# ================================================================

def app_edit_holding(
    ticker,
    new_value
):

    df = load_portfolio_database()

    ticker_col = portfolio_ticker_column(df)
    value_col = portfolio_value_column(df)

    if ticker_col is None or value_col is None:
        return False, "Portfolio columns unavailable."

    ticker = str(ticker).strip().upper()

    mask = (
        df[ticker_col]
        .astype(str)
        .str.upper()
        == ticker
    )

    if not mask.any():
        return False, f"{ticker} not found."

    if new_value < 0:
        return False, "Value cannot be negative."

    idx = df[mask].index[0]

    df.loc[idx, value_col] = float(new_value)

    save_portfolio_database(df)

    return (
        True,
        f"{ticker} updated."
    )


# ================================================================
# PORTFOLIO MANAGEMENT UI
# ================================================================

def render_portfolio_manager():

    st.markdown("---")

    st.markdown(
        '<div class="section-heading">'
        'Manage Portfolio'
        '</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Record changes to your real portfolio here. "
        "These controls do not execute brokerage trades."
    )


    tab_add, tab_more, tab_sell, tab_edit = st.tabs(
        [
            "＋ Add Holding",
            "↑ Buy More",
            "− Record Sale",
            "✎ Edit Holding"
        ]
    )


    # ------------------------------------------------------------
    # ADD
    # ------------------------------------------------------------

    with tab_add:

        with st.form("add_holding_form"):

            ticker = st.text_input(
                "Ticker",
                placeholder="e.g. CVX"
            )

            value = st.number_input(
                "Current value (£)",
                min_value=0.0,
                step=100.0
            )

            sector = st.text_input(
                "Sector / Category",
                placeholder="Optional"
            )

            submitted = st.form_submit_button(
                "Add Holding",
                use_container_width=True
            )


            if submitted:

                ok, message = app_add_holding(
                    ticker,
                    value,
                    sector
                )

                if ok:
                    st.success(message)
                    st.session_state[
                        "portfolio_changed"
                    ] = True

                else:
                    st.error(message)


    # ------------------------------------------------------------
    # CURRENT ACTIVE TICKERS
    # ------------------------------------------------------------

    live_df = load_portfolio_database()

    ticker_col = portfolio_ticker_column(
        live_df
    )

    active_col = portfolio_active_column(
        live_df
    )

    if (
        active_col
        and active_col in live_df.columns
    ):

        active_mask = (
            live_df[active_col]
            .astype(str)
            .str.lower()
            .isin(
                ["true", "1", "yes", "held"]
            )
        )

        active_df = live_df[
            active_mask
        ].copy()

    else:

        active_df = live_df.copy()


    if ticker_col:

        ticker_options = sorted(
            active_df[ticker_col]
            .dropna()
            .astype(str)
            .tolist()
        )

    else:

        ticker_options = []


    # ------------------------------------------------------------
    # BUY MORE
    # ------------------------------------------------------------

    with tab_more:

        if not ticker_options:

            st.info(
                "No active holdings available."
            )

        else:

            with st.form("buy_more_form"):

                ticker = st.selectbox(
                    "Holding",
                    ticker_options,
                    key="buy_more_ticker"
                )

                amount = st.number_input(
                    "Additional value (£)",
                    min_value=0.0,
                    step=100.0,
                    key="buy_more_value"
                )

                submitted = (
                    st.form_submit_button(
                        "Record Buy More",
                        use_container_width=True
                    )
                )


                if submitted:

                    ok, message = app_buy_more(
                        ticker,
                        amount
                    )

                    if ok:

                        st.success(message)

                        st.session_state[
                            "portfolio_changed"
                        ] = True

                    else:

                        st.error(message)


    # ------------------------------------------------------------
    # SELL
    # ------------------------------------------------------------

    with tab_sell:

        if not ticker_options:

            st.info(
                "No active holdings available."
            )

        else:

            with st.form("sell_form"):

                ticker = st.selectbox(
                    "Holding",
                    ticker_options,
                    key="sell_ticker"
                )

                amount = st.number_input(
                    "Value sold (£)",
                    min_value=0.0,
                    step=100.0,
                    key="sell_value"
                )

                st.caption(
                    "Entering the full current value "
                    "marks the holding as sold."
                )

                submitted = (
                    st.form_submit_button(
                        "Record Sale",
                        use_container_width=True
                    )
                )


                if submitted:

                    ok, message = app_record_sale(
                        ticker,
                        amount
                    )

                    if ok:

                        st.success(message)

                        st.session_state[
                            "portfolio_changed"
                        ] = True

                    else:

                        st.error(message)


    # ------------------------------------------------------------
    # EDIT
    # ------------------------------------------------------------

    with tab_edit:

        if not ticker_options:

            st.info(
                "No active holdings available."
            )

        else:

            with st.form("edit_form"):

                ticker = st.selectbox(
                    "Holding",
                    ticker_options,
                    key="edit_ticker"
                )

                new_value = st.number_input(
                    "Correct current value (£)",
                    min_value=0.0,
                    step=100.0,
                    key="edit_value"
                )

                submitted = (
                    st.form_submit_button(
                        "Update Holding",
                        use_container_width=True
                    )
                )


                if submitted:

                    ok, message = app_edit_holding(
                        ticker,
                        new_value
                    )

                    if ok:

                        st.success(message)

                        st.session_state[
                            "portfolio_changed"
                        ] = True

                    else:

                        st.error(message)


    # ------------------------------------------------------------
    # CHANGE NOTICE
    # ------------------------------------------------------------

    if st.session_state.get(
        "portfolio_changed",
        False
    ):

        st.warning(
            "Portfolio changed. Recommendations may be stale."
        )

        if st.button(
            "Refresh Investment Intelligence",
            type="primary",
            use_container_width=True
        ):

            refresh_live_intelligence()


    if st.session_state.get(
        "last_refresh_message"
    ):

        st.success(
            st.session_state[
                "last_refresh_message"
            ]
        )

        st.session_state[
            "last_refresh_message"
        ] = None



# ================================================================
# DYNAMIC PORTFOLIO INTELLIGENCE
# ================================================================

def active_ticker_set():

    df = load_portfolio_database()

    if df.empty:
        return set()

    ticker_col = portfolio_ticker_column(df)
    active_col = portfolio_active_column(df)

    if ticker_col is None:
        return set()

    if active_col:

        mask = (
            df[active_col]
            .astype(str)
            .str.lower()
            .isin(
                [
                    "true",
                    "1",
                    "yes",
                    "held"
                ]
            )
        )

        df = df[mask].copy()

    return set(
        df[ticker_col]
        .dropna()
        .astype(str)
        .str.upper()
        .str.strip()
    )


def dynamic_master_table():

    if master_investment.empty:
        return pd.DataFrame()

    df = master_investment.copy()

    ticker_col = find_ticker_column(df)
    score_col = find_score_column(df)

    if ticker_col is None:
        return df

    held = active_ticker_set()

    df["App_Ticker"] = (
        df[ticker_col]
        .astype(str)
        .str.upper()
        .str.strip()
    )

    df["Currently_Held_Live"] = (
        df["App_Ticker"]
        .isin(held)
    )

    if score_col:

        df["_Live_Score"] = pd.to_numeric(
            df[score_col],
            errors="coerce"
        )

    else:

        df["_Live_Score"] = 0


    # ------------------------------------------------------------
    # LIVE ACTION CLASSIFICATION
    # ------------------------------------------------------------

    def classify(row):

        score = row["_Live_Score"]
        held_now = row["Currently_Held_Live"]

        if pd.isna(score):
            return "WATCH"

        if held_now:

            if score >= 8.0:
                return "ADD / BUY MORE"

            elif score >= 6.0:
                return "HOLD"

            elif score >= 4.5:
                return "HOLD / REVIEW"

            else:
                return "REVIEW"

        else:

            if score >= 8.0:
                return "BUY NEW"

            elif score >= 6.5:
                return "WATCH / BUY"

            else:
                return "WATCH"


    df["Live_Action"] = df.apply(
        classify,
        axis=1
    )

    return df


def dynamic_top5_overall():

    df = dynamic_master_table()

    if df.empty:
        return df

    return (
        df
        .sort_values(
            "_Live_Score",
            ascending=False
        )
        .head(5)
        .copy()
    )


def dynamic_top5_new():

    df = dynamic_master_table()

    if df.empty:
        return df

    return (
        df[
            df["Live_Action"] == "BUY NEW"
        ]
        .sort_values(
            "_Live_Score",
            ascending=False
        )
        .head(5)
        .copy()
    )


def dynamic_buy_more():

    df = dynamic_master_table()

    if df.empty:
        return df

    return (
        df[
            df["Live_Action"]
            == "ADD / BUY MORE"
        ]
        .sort_values(
            "_Live_Score",
            ascending=False
        )
        .head(5)
        .copy()
    )


def dynamic_top_holdings():

    df = dynamic_master_table()

    if df.empty:
        return df

    return (
        df[
            df["Currently_Held_Live"]
        ]
        .sort_values(
            "_Live_Score",
            ascending=False
        )
        .head(5)
        .copy()
    )


def dynamic_review_holdings():

    df = dynamic_master_table()

    if df.empty:
        return df

    return (
        df[
            df["Live_Action"].isin(
                [
                    "REVIEW",
                    "HOLD / REVIEW"
                ]
            )
        ]
        .sort_values(
            "_Live_Score",
            ascending=True
        )
        .head(5)
        .copy()
    )


def dynamic_rotation_table():

    if rotation_moves.empty:
        return pd.DataFrame()

    df = rotation_moves.copy()

    held = active_ticker_set()

    holding_col = first_existing_column(
        df,
        [
            "Holding",
            "Sell",
            "Current",
            "Current_Ticker",
            "Sell_Ticker"
        ]
    )

    if holding_col is None:
        return df

    df["_Holding_Live"] = (
        df[holding_col]
        .astype(str)
        .str.upper()
        .str.strip()
    )

    # Only keep rotation ideas for things
    # still actually held
    df = df[
        df["_Holding_Live"]
        .isin(held)
    ].copy()

    return df


def refresh_live_intelligence():

    st.cache_data.clear()

    st.session_state[
        "portfolio_changed"
    ] = False

    st.session_state[
        "last_refresh_message"
    ] = (
        "Portfolio intelligence refreshed."
    )

    st.rerun()



# ================================================================
# REAL PAGE VIEWS
# ================================================================

def render_ranked_list(
    df,
    title,
    action_text=None,
    limit=5
):

    st.markdown(
        f'<div class="section-heading">{title}</div>',
        unsafe_allow_html=True
    )

    if df is None or df.empty:

        st.info(
            "No qualifying results."
        )

        return

    ticker_col = find_ticker_column(df)
    score_col = find_score_column(df)

    display_df = df.copy().head(limit)

    for i, (_, row) in enumerate(
        display_df.iterrows(),
        start=1
    ):

        ticker = (
            str(row[ticker_col])
            if ticker_col
            else "—"
        )

        try:
            score = float(row[score_col])
            score_text = f"{score:.1f}/10"
        except:
            score_text = "—"

        status = ""

        if action_text:
            status = f"   {action_text}"

        top5_html = f"""
            <div style="
                padding:12px 4px;
                border-bottom:1px solid {theme['border']};
                font-size:15px;
            ">
                <b>{i}. {ticker}</b>

                <span style="
                    float:right;
                    color:{theme['accent']};
                    font-weight:700;
                ">
                    {score_text}
                </span>

                <br>

                <span style="
                    color:{theme['muted']};
                    font-size:12px;
                ">
                    {status}
                </span>

            </div>
        """

        st.html(
            textwrap.dedent(
                top5_html
            ).strip()
        )


def render_table_section(
    df,
    title,
    empty_message="No data available.",
    rows=None
):

    st.markdown(
        f'<div class="section-heading">{title}</div>',
        unsafe_allow_html=True
    )

    show_engine_table(
        df,
        empty_message=empty_message,
        rows=rows
    )


# ================================================================
# DASHBOARD PAGE
# ================================================================

def page_dashboard():

    top5_overall_live = dynamic_top5_overall()
    top5_new_live = dynamic_top5_new()
    buy_more_live = dynamic_buy_more()
    top5_holdings_live = dynamic_top_holdings()
    review_holdings_live = dynamic_review_holdings()
    actionable_rotation_live = dynamic_rotation_table()

    best_ticker, best_score = (
        top_opportunity()
    )

    best_text = (
        f"{best_ticker} {best_score:.1f}/10"
        if best_score is not None
        else best_ticker
    )

    growth_text = (
        f"{portfolio_growth:+.2f}%"
        if portfolio_growth is not None
        else "—"
    )



    c1, c2, c3 = st.columns(3)


    with c1:

        aiia_metric_card(
            "Portfolio Value",
            f"£{total_value:,.2f}",
            "Current portfolio value"
        )


    with c2:

        aiia_metric_card(
            "Top Opportunity",
            best_text,
            "Great Investment ranking"
        )


    with c3:

        aiia_metric_card(
            "Growth",
            portfolio_growth_text,
            portfolio_growth_detail,
            portfolio_growth_direction
        )


    st.write("")


    left, right = st.columns(
        [1.25, 1]
    )


    with left:

        st.markdown(
            '<div class="section-card">',
            unsafe_allow_html=True
        )

        render_ranked_list(
            top5_overall_live,
            "Top 5 Opportunities",
            limit=5
        )

        if st.button(
            "View Top 5",
            use_container_width=True
        ):

            st.session_state.page = "Top 5"
            st.rerun()

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


    with right:

        st.markdown(
            '<div class="section-card">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-heading">Portfolio Health</div>',
            unsafe_allow_html=True
        )

        strongest = "—"

        if not top5_holdings_live.empty:

            tcol = find_ticker_column(
                top5_holdings
            )

            scol = find_score_column(
                top5_holdings
            )

            if tcol:

                strongest = str(
                    top5_holdings_live.iloc[0][tcol]
                )

                if scol:

                    try:

                        strongest += (
                            f" "
                            f"{float(top5_holdings_live.iloc[0][scol]):.1f}/10"
                        )

                    except:
                        pass


        st.write(
            f"**Strongest holding:** {strongest}"
        )

        st.write(
            f"**Holdings to review:** "
            f"{len(review_holdings_live)}"
        )

        st.write(
            f"**Buy-more opportunities:** "
            f"{len(buy_more_live)}"
        )

        st.write(
            f"**Rotation candidates:** "
            f"{len(actionable_rotation_live)}"
        )


        if st.button(
            "View My Portfolio",
            use_container_width=True
        ):

            st.session_state.page = (
                "My Portfolio"
            )

            st.rerun()


        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


    st.write("")


    left2, right2 = st.columns(2)


    with left2:

        st.markdown(
            '<div class="section-card">',
            unsafe_allow_html=True
        )

        render_ranked_list(
            top5_new_live,
            "Best New Opportunities",
            action_text="BUY NEW",
            limit=3
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


    with right2:

        st.markdown(
            '<div class="section-card">',
            unsafe_allow_html=True
        )

        render_ranked_list(
            review_holdings_live,
            "Attention Required",
            action_text="REVIEW",
            limit=3
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# ================================================================
# MY PORTFOLIO PAGE
# ================================================================

def page_portfolio():

    st.markdown(
        '<div class="section-heading">My Portfolio</div>',
        unsafe_allow_html=True
    )


    c1, c2, c3 = st.columns(3)


    with c1:

        aiia_metric_card(
            "Portfolio Value",
            f"£{total_value:,.2f}",
            "Current portfolio value"
        )


    with c2:

        aiia_metric_card(
            "Growth",
            portfolio_growth_text,
            portfolio_growth_detail,
            portfolio_growth_direction
        )


    with c3:

        aiia_metric_card(
            "Active Positions",
            f"{len(portfolio)}",
            "Currently held investments"
        )


    st.write("")



    render_table_section(
        portfolio,
        "Current Holdings",
        "No active holdings."
    )


    st.write("")


    render_table_section(
        sector_exposure,
        "Portfolio Exposure",
        "Sector exposure unavailable."
    )


    # Portfolio editing controls
    render_portfolio_manager()


# ================================================================
# TOP 5 PAGE
# ================================================================

def page_top5():

    top5_overall_live = dynamic_top5_overall()
    top5_new_live = dynamic_top5_new()
    buy_more_live = dynamic_buy_more()
    top5_holdings_live = dynamic_top_holdings()

    st.markdown(
        '<div class="section-heading">Top 5 Investment Opportunities</div>',
        unsafe_allow_html=True
    )


    c1, c2 = st.columns(2)


    with c1:

        st.markdown(
            '<div class="section-card">',
            unsafe_allow_html=True
        )

        render_ranked_list(
            top5_overall_live,
            "Overall Top 5",
            limit=5
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


    with c2:

        st.markdown(
            '<div class="section-card">',
            unsafe_allow_html=True
        )

        render_ranked_list(
            top5_new_live,
            "Best New Buys",
            action_text="BUY NEW",
            limit=5
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


    st.write("")


    c3, c4 = st.columns(2)


    with c3:

        st.markdown(
            '<div class="section-card">',
            unsafe_allow_html=True
        )

        if buy_more_live.empty:

            st.markdown(
                '<div class="section-heading">Add / Buy More</div>',
                unsafe_allow_html=True
            )

            st.info(
                "No existing holdings currently qualify "
                "for ADD / BUY MORE."
            )

        else:

            render_ranked_list(
                buy_more_live,
                "Add / Buy More",
                action_text="ADD",
                limit=5
            )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


    with c4:

        st.markdown(
            '<div class="section-card">',
            unsafe_allow_html=True
        )

        render_ranked_list(
            top5_holdings_live,
            "Strongest Current Holdings",
            action_text="HOLD",
            limit=5
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# ================================================================
# DISCOVER PAGE
# ================================================================

def page_discover():

    st.markdown(
        '<div class="section-heading">Discover</div>',
        unsafe_allow_html=True
    )


    search = st.text_input(
        "Search ticker",
        placeholder="e.g. CVX"
    )


    source = (
        investable_discovery.copy()
        if not investable_discovery.empty
        else deep_discovery.copy()
    )


    if search and not source.empty:

        ticker_col = (
            find_ticker_column(source)
        )

        if ticker_col:

            source = source[
                source[ticker_col]
                .astype(str)
                .str.upper()
                .str.contains(
                    search.upper(),
                    na=False
                )
            ]


    render_table_section(
        source,
        "Investment Discovery",
        "No discovery results available.",
        rows=50
    )


# ================================================================
# ROTATION PAGE
# ================================================================

def page_rotation():

    actionable_rotation_live = dynamic_rotation_table()

    st.markdown(
        '<div class="section-heading">Capital Rotation</div>',
        unsafe_allow_html=True
    )


    st.warning(
        "Secondary decision support only. "
        "Great Investment remains the primary investment signal."
    )


    render_table_section(
        actionable_rotation_live,
        "Highest-Conviction Rotation Opportunities",
        "No actionable rotation opportunities."
    )


    st.write("")


    with st.expander(
        "View full opportunity-cost analysis"
    ):

        show_engine_table(
            rotation_moves,
            empty_message=(
                "No rotation analysis available."
            ),
            rows=30
        )


# ================================================================
# SETTINGS PAGE
# ================================================================

def page_settings():

    st.markdown(
        '<div class="section-heading">Settings</div>',
        unsafe_allow_html=True
    )


    new_theme = st.selectbox(

        "Theme",

        [
            "Eggshell",
            "Natural",
            "Future"
        ],

        index=[
            "Eggshell",
            "Natural",
            "Future"
        ].index(
            st.session_state.theme
        )
    )


    if new_theme != st.session_state.theme:

        st.session_state.theme = new_theme
        st.rerun()


    st.markdown("---")

    st.write("### Analysis")

    st.write(
        "Market refresh: **Daily**"
    )

    st.write(
        "Discovery universe: **Broad Market**"
    )

    st.write(
        "Recovery protection: **Active**"
    )

    st.write(
        "Rotation analysis: **Active**"
    )


    st.markdown("---")

    st.write("### Display")

    st.write(
        "Currency: **GBP**"
    )

    st.write(
        f"Theme: **{st.session_state.theme}**"
    )

    st.write(
        "Detail level: **Standard**"
    )


# ================================================================
# PAGE ROUTER
# ================================================================

if st.session_state.page == "Dashboard":

    page_dashboard()


elif st.session_state.page == "My Portfolio":

    page_portfolio()


elif st.session_state.page == "Top 5":

    page_top5()


elif st.session_state.page == "Discover":

    page_discover()


elif st.session_state.page == "Rotation":

    page_rotation()


elif st.session_state.page == "Settings":

    page_settings()



# ================================================================
# FOOTER
# ================================================================

st.markdown(
    """
    <div class="deco-rule">
        <span class="deco-diamond"></span>
    </div>
    """,
    unsafe_allow_html=True
)

st.caption(
    "MY INVESTMENT AI  •  Decision Support  •  "
    "Great Investment is the primary signal"
)

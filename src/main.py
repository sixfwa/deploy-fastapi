import fastapi as _fastapi
import service as _service
import starlette.responses as _responses

app = _fastapi.FastAPI()


@app.get("/")
async def root():
    return _responses.RedirectResponse("/redoc")


@app.get("/events/today")
async def today():
    return _service.todays_events()


@app.get("/events")
async def events():
    return _service.get_all_events()


@app.get("/events/{month}")
async def events_month(month: str):
    month_events = _service.month_events(month)
    if month_events:
        return month_events

    return _fastapi.HTTPException(
        status_code=404, detail=f"Month: {month} could not be found"
    )


@app.get("/events/{month}/{day}")
async def events_of_day(month: str, day: int):
    events = _service.day_events(month, day)
    if events:
        return events

    return _fastapi.HTTPException(
        status_code=404, detail=f"Date: {month}/{day} could not be found"
    )

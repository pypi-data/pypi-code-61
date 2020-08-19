eventid=20200727
client='icici'

def dashboard(phase):
    from mathlogic import get_leaderboard
    if phase in ('binary.classification','regression'):
        get_leaderboard(eventid=eventid,client=client,phase=phase,return_format="display_html")
    else:
        print("No such Phase or Problem for current event")

def evaluate(indf,phase):
    from mathlogic import evaluate_result
    ## This portion needs to be updated for every Training/ Event
    if phase in ('binary.classification','regression'):
        if phase=='binary.classification':
            metric='LogLoss'
            pred_cols = ['id','y_pred_0','y_pred_1']
            act_file=str(eventid)+"_"+client+"_"+phase+"_key.csv"
        elif phase=='regression':
            metric='RMSE'
            pred_cols = ['id','y_pred']
            act_file=str(eventid)+"_"+client+"_"+phase+"_key.csv"
        elif phase=='multilabel.text.classification':
            metric='BinaryCrossEntropy'
            pred_cols = ['id','y_pred_0','y_pred_1','y_pred_2','y_pred_3']
            act_file=str(eventid)+"_"+client+"_"+phase+"_key.csv"
    else:
        print("No such Phase or Problem for current event")
    evaluate_result(indf,eventid=eventid,client=client,phase=phase,metric=metric,act_file=act_file,pred_cols=pred_cols)

